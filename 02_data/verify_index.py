"""Verify downloaded Kaggle STEP-003 outputs (ds0001_index.csv & ds0001_audit_summary.json)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = [
    "image_id",
    "rel_path",
    "label",
    "label_name",
    "generator",
    "width",
    "height",
    "file_ext",
    "md5_hash",
]


def verify(data_dir: Path = Path("02_data")) -> int:
    index_path = data_dir / "ds0001_index.csv"
    summary_path = data_dir / "ds0001_audit_summary.json"

    if not index_path.is_file():
        print(f"[MISSING] {index_path} — run 04_notebooks/01_ds0001_audit_and_index.ipynb on Kaggle and place output here.")
        return 1
    if not summary_path.is_file():
        print(f"[MISSING] {summary_path} — run 04_notebooks/01_ds0001_audit_and_index.ipynb on Kaggle and place output here.")
        return 1

    df = pd.read_csv(index_path)
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        print(f"[FAIL] Missing columns in ds0001_index.csv: {missing_cols}")
        return 1

    with summary_path.open("r", encoding="utf-8") as f:
        summary = json.load(f)

    total = len(df)
    n_real = int((df["label"] == 0).sum())
    n_fake = int((df["label"] == 1).sum())
    n_gens = int(df.loc[df["label"] == 1, "generator"].nunique())
    n_null = int(df[REQUIRED_COLUMNS].isna().sum().sum())
    n_unique_paths = int(df["rel_path"].nunique())

    print(f"Total rows      : {total}")
    print(f"Real / Fake     : {n_real} / {n_fake}")
    print(f"Fake generators : {n_gens}")
    print(f"Unique paths    : {n_unique_paths}")
    print(f"Null cells      : {n_null}")
    print(f"Corrupt count   : {summary.get('corrupt_count')}")
    print(f"Duplicate MD5s  : {summary.get('duplicate_md5_groups')}")

    assert total == 50000, f"Expected 50000 rows, got {total}"
    assert n_real == 25000 and n_fake == 25000, f"Expected 25000/25000 split, got {n_real}/{n_fake}"
    assert n_gens == 13, f"Expected 13 fake generators, got {n_gens}"
    assert n_null == 0, f"Found {n_null} null values"
    assert n_unique_paths == 50000, f"Duplicate rel_path detected ({n_unique_paths}/50000)"
    assert summary.get("corrupt_count", -1) == 0, f"Non-zero corrupt count: {summary.get('corrupt_count')}"

    print("[PASS] STEP-003 DS0001 index & audit summary verified 100%.")
    return 0


if __name__ == "__main__":
    sys.exit(verify())
