"""STEP-006: Reusable preprocessing and strictly training-only augmentation pipelines."""

from __future__ import annotations

import io
import random
from typing import Tuple

from PIL import Image, ImageFilter

try:
    import torch
    from torchvision import transforms
except ImportError:  # pragma: no cover - local CPU envs without torchvision
    torch = None  # type: ignore
    transforms = None  # type: ignore

IMAGENET_MEAN: Tuple[float, float, float] = (0.485, 0.456, 0.406)
IMAGENET_STD: Tuple[float, float, float] = (0.229, 0.224, 0.225)


class EnsureRGB:
    """Convert any PIL image (RGBA, L, P, CMYK) safely to 3-channel RGB."""

    def __call__(self, img: Image.Image) -> Image.Image:
        return img.convert("RGB") if img.mode != "RGB" else img


class RandomJPEGCompression:
    """Simulate real-world web / mobile e-KYC JPEG recompression (training-only)."""

    def __init__(self, quality_min: int = 40, quality_max: int = 95, p: float = 0.5) -> None:
        if not (1 <= quality_min <= quality_max <= 100):
            raise ValueError("JPEG quality range must satisfy 1 <= min <= max <= 100.")
        self.quality_min = quality_min
        self.quality_max = quality_max
        self.p = p

    def __call__(self, img: Image.Image) -> Image.Image:
        if random.random() >= self.p:
            return img
        rgb = img.convert("RGB") if img.mode != "RGB" else img
        quality = random.randint(self.quality_min, self.quality_max)
        buf = io.BytesIO()
        rgb.save(buf, format="JPEG", quality=quality)
        buf.seek(0)
        with Image.open(buf) as decoded:
            return decoded.convert("RGB")


class DeterministicJPEGAndBlur:
    """Deterministic degradation transform for STEP-012 robustness evaluation."""

    def __init__(self, jpeg_quality: int = 60, blur_radius: float = 0.8) -> None:
        self.jpeg_quality = jpeg_quality
        self.blur_radius = blur_radius

    def __call__(self, img: Image.Image) -> Image.Image:
        rgb = img.convert("RGB") if img.mode != "RGB" else img
        if self.blur_radius > 0:
            rgb = rgb.filter(ImageFilter.GaussianBlur(radius=self.blur_radius))
        buf = io.BytesIO()
        rgb.save(buf, format="JPEG", quality=self.jpeg_quality)
        buf.seek(0)
        with Image.open(buf) as decoded:
            return decoded.convert("RGB")


def get_eval_transforms(img_size: int = 224) -> transforms.Compose:
    """Strictly deterministic preprocessing for validation, testing, and app inference."""
    return transforms.Compose(
        [
            EnsureRGB(),
            transforms.Resize((img_size, img_size), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def get_degraded_eval_transforms(
    img_size: int = 224,
    jpeg_quality: int = 60,
    blur_radius: float = 0.8,
) -> transforms.Compose:
    """Deterministic compressed+blurred test transform to benchmark real-world e-KYC robustness."""
    return transforms.Compose(
        [
            EnsureRGB(),
            DeterministicJPEGAndBlur(jpeg_quality=jpeg_quality, blur_radius=blur_radius),
            transforms.Resize((img_size, img_size), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def get_train_transforms_basic(img_size: int = 224) -> transforms.Compose:
    """Basic training-only augmentation used for Part 3 baseline models (M2–M4)."""
    return transforms.Compose(
        [
            EnsureRGB(),
            transforms.Resize((img_size, img_size), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def get_train_transforms_robust(img_size: int = 224) -> transforms.Compose:
    """Robustness-oriented training-only augmentation (JPEG + Blur + ColorJitter) for STEP-012."""
    return transforms.Compose(
        [
            EnsureRGB(),
            transforms.Resize((img_size, img_size), interpolation=transforms.InterpolationMode.BICUBIC),
            transforms.RandomHorizontalFlip(p=0.5),
            RandomJPEGCompression(quality_min=40, quality_max=95, p=0.5),
            transforms.RandomApply(
                [transforms.GaussianBlur(kernel_size=3, sigma=(0.1, 1.5))],
                p=0.3,
            ),
            transforms.RandomApply(
                [transforms.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.10, hue=0.02)],
                p=0.4,
            ),
            transforms.ToTensor(),
            transforms.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD),
        ]
    )


def denormalize_tensor(tensor: torch.Tensor) -> torch.Tensor:
    """Invert ImageNet normalization back to [0, 1] RGB tensor for visualization."""
    mean = torch.tensor(IMAGENET_MEAN, device=tensor.device, dtype=tensor.dtype).view(-1, 1, 1)
    std = torch.tensor(IMAGENET_STD, device=tensor.device, dtype=tensor.dtype).view(-1, 1, 1)
    return (tensor * std + mean).clamp(0.0, 1.0)
