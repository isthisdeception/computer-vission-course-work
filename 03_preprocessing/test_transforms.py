"""Unit tests for STEP-005 splits and STEP-006 preprocessing/augmentation transforms."""

from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import pandas as pd
import pytest
from PIL import Image

try:
    import torch
    import torchvision  # noqa: F401
    HAS_TORCHVISION = True
except ImportError:
    torch = None  # type: ignore
    HAS_TORCHVISION = False

from transforms import (
    DeterministicJPEGAndBlur,
    RandomJPEGCompression,
    denormalize_tensor,
    get_degraded_eval_transforms,
    get_eval_transforms,
    get_train_transforms_basic,
    get_train_transforms_robust,
)


def _dummy_image(mode: str = "RGB", size: tuple[int, int] = (200, 200)) -> Image.Image:
    rng = np.random.default_rng(42)
    if mode == "L":
        arr = rng.integers(0, 256, size=(size[1], size[0]), dtype=np.uint8)
    elif mode == "RGBA":
        arr = rng.integers(0, 256, size=(size[1], size[0], 4), dtype=np.uint8)
    else:
        arr = rng.integers(0, 256, size=(size[1], size[0], 3), dtype=np.uint8)
    return Image.fromarray(arr, mode=mode)


@pytest.mark.skipif(not HAS_TORCHVISION, reason="torchvision not installed in local env; verified on Kaggle")
def test_eval_transforms_are_strictly_deterministic():
    img = _dummy_image("RGB")
    tf = get_eval_transforms(img_size=224)
    out1 = tf(img)
    out2 = tf(img)
    assert out1.shape == (3, 224, 224)
    assert out1.dtype == torch.float32
    assert torch.equal(out1, out2), "Eval transforms must be 100% deterministic!"


@pytest.mark.skipif(not HAS_TORCHVISION, reason="torchvision not installed in local env; verified on Kaggle")
def test_degraded_eval_transforms_are_deterministic():
    img = _dummy_image("RGB")
    tf = get_degraded_eval_transforms(img_size=224, jpeg_quality=60, blur_radius=0.8)
    out1 = tf(img)
    out2 = tf(img)
    assert out1.shape == (3, 224, 224)
    assert torch.equal(out1, out2), "Degraded eval transforms must be deterministic!"


@pytest.mark.skipif(not HAS_TORCHVISION, reason="torchvision not installed in local env; verified on Kaggle")
def test_color_mode_safety_and_denormalize():
    tf = get_eval_transforms(img_size=224)
    for mode in ("RGB", "RGBA", "L"):
        t = tf(_dummy_image(mode))
        assert t.shape == (3, 224, 224)
        assert torch.isfinite(t).all()
        denorm = denormalize_tensor(t)
        assert float(denorm.min()) >= 0.0 and float(denorm.max()) <= 1.0


@pytest.mark.skipif(not HAS_TORCHVISION, reason="torchvision not installed in local env; verified on Kaggle")
def test_train_transforms_basic_and_robust():
    img = _dummy_image("RGB")
    random.seed(42)
    torch.manual_seed(42)
    for tf in (get_train_transforms_basic(224), get_train_transforms_robust(224)):
        t = tf(img)
        assert t.shape == (3, 224, 224)
        assert t.dtype == torch.float32
        assert torch.isfinite(t).all()


def test_deterministic_jpeg_and_blur():
    img = _dummy_image("RGB")
    deg = DeterministicJPEGAndBlur(jpeg_quality=60, blur_radius=0.8)
    out1 = deg(img)
    out2 = deg(img)
    assert out1.size == img.size and out1.mode == "RGB"
    assert np.array_equal(np.asarray(out1), np.asarray(out2))


def test_random_jpeg_compression_modifies_pixels():
    img = _dummy_image("RGB")
    comp = RandomJPEGCompression(quality_min=40, quality_max=45, p=1.0)
    out = comp(img)
    assert out.size == img.size and out.mode == "RGB"
    assert not np.array_equal(np.asarray(img), np.asarray(out))


def test_frozen_splits_zero_leakage():
    std_path = Path("02_data/splits/ds0001_split_v1.csv")
    unseen_path = Path("02_data/splits/ds0001_unseen_gen_split.csv")
    assert std_path.is_file(), "Run 03_preprocessing/create_splits.py first."
    assert unseen_path.is_file(), "Run 03_preprocessing/create_splits.py first."

    df = pd.read_csv(std_path)
    assert len(df) == 50000
    assert (df["split"] == "train").sum() == 35000
    assert (df["split"] == "val").sum() == 7500
    assert (df["split"] == "test").sum() == 7500
    for col in ("image_id", "rel_path", "md5_hash"):
        sets = [set(df.loc[df["split"] == s, col]) for s in ("train", "val", "test")]
        assert sets[0].isdisjoint(sets[1])
        assert sets[0].isdisjoint(sets[2])
        assert sets[1].isdisjoint(sets[2])

    udf = pd.read_csv(unseen_path)
    tv_gens = set(udf.loc[udf["split"] != "test", "generator"])
    assert "stable_diffusion" not in tv_gens
    assert "stylegan3" not in tv_gens
