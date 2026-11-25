"""STEP-006: PyTorch Dataset and DataLoader factory for DS0001 frozen splits."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Dict, Optional, Tuple

import pandas as pd
import torch
from PIL import Image
from torch.utils.data import DataLoader, Dataset

from .transforms import (
    get_eval_transforms,
    get_train_transforms_basic,
    get_train_transforms_robust,
)


class DS0001Dataset(Dataset):
    """Dataset wrapper reading a frozen split CSV + Kaggle DS0001 root directory."""

    def __init__(
        self,
        split_csv: Path | str,
        data_root: Path | str,
        split: str,
        transform: Optional[Callable] = None,
        return_meta: bool = False,
    ) -> None:
        if split not in ("train", "val", "test"):
            raise ValueError(f"Invalid split '{split}'. Expected 'train', 'val', or 'test'.")
        df = pd.read_csv(split_csv)
        self.df = df[df["split"] == split].reset_index(drop=True)
        self.data_root = Path(data_root)
        self.split = split
        self.transform = transform or get_eval_transforms()
        self.return_meta = return_meta

    def __len__(self) -> int:
        return len(self.df)

    def __getitem__(self, idx: int):
        row = self.df.iloc[idx]
        img_path = self.data_root / row["rel_path"]
        with Image.open(img_path) as im:
            rgb = im.convert("RGB")
        tensor = self.transform(rgb)
        label = torch.tensor(int(row["label"]), dtype=torch.long)

        if self.return_meta:
            meta = {
                "image_id": str(row["image_id"]),
                "rel_path": str(row["rel_path"]),
                "generator": str(row["generator"]),
                "label_name": str(row["label_name"]),
            }
            return tensor, label, meta
        return tensor, label


def build_dataloaders(
    split_csv: Path | str,
    data_root: Path | str,
    *,
    img_size: int = 224,
    aug_mode: str = "basic",
    batch_size: int = 64,
    num_workers: int = 4,
    pin_memory: bool = True,
    return_meta_eval: bool = False,
) -> Dict[str, DataLoader]:
    """Create train/val/test DataLoaders enforcing strictly training-only augmentation."""
    if aug_mode == "basic":
        train_tf = get_train_transforms_basic(img_size=img_size)
    elif aug_mode == "robust":
        train_tf = get_train_transforms_robust(img_size=img_size)
    elif aug_mode == "none":
        train_tf = get_eval_transforms(img_size=img_size)
    else:
        raise ValueError(f"Unknown aug_mode='{aug_mode}'. Choose 'basic', 'robust', or 'none'.")

    eval_tf = get_eval_transforms(img_size=img_size)

    train_ds = DS0001Dataset(split_csv, data_root, split="train", transform=train_tf, return_meta=False)
    val_ds = DS0001Dataset(split_csv, data_root, split="val", transform=eval_tf, return_meta=return_meta_eval)
    test_ds = DS0001Dataset(split_csv, data_root, split="test", transform=eval_tf, return_meta=return_meta_eval)

    return {
        "train": DataLoader(
            train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers, pin_memory=pin_memory, drop_last=False
        ),
        "val": DataLoader(
            val_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=pin_memory, drop_last=False
        ),
        "test": DataLoader(
            test_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=pin_memory, drop_last=False
        ),
    }
