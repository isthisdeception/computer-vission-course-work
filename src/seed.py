"""Global deterministic seeding helper for reproducible experiments."""

from __future__ import annotations

import os
import random
from typing import Optional

import numpy as np

SEED: int = 42


def set_global_seed(seed: int = SEED, deterministic_cudnn: bool = True) -> int:
    """Seed Python, NumPy, and PyTorch (if installed) for reproducibility.

    Parameters
    ----------
    seed : int
        Integer random seed (default: 42).
    deterministic_cudnn : bool
        If True, enables deterministic cuDNN algorithms when PyTorch is available.

    Returns
    -------
    int
        The seed that was applied.
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)
        if deterministic_cudnn:
            torch.backends.cudnn.deterministic = True
            torch.backends.cudnn.benchmark = False
    except ImportError:
        pass

    return seed
