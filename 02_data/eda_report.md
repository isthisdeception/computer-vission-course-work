# Visual Exploratory Data Analysis Report — `DS0001` (`STEP-004`)

> **Owner:** Member 2 — Khadijatul Kobra Keya (`0242310005101223`)  
> **Source Notebook:** `04_notebooks/02_visual_eda.ipynb`  
> **Stratified Pixel/FFT Sample:** `n = 4,000` (`2,000` Real + `2,000` Fake balanced across all 13 generators, `SEED = 42`)  

## 1. Class Balance & Split Integrity (`fig01`)
- Total verified images: **50,000** (`25,000` Real / `25,000` AI-Generated Fake — exact `50.0% / 50.0%` balance).
- Synthetic faces are near-uniformly distributed across **13 distinct generators** (`1,923` each; `stylegan2` = `1,924`).
- Frozen leak-free splits (`ds0001_split_v1.csv`): **35,000 Train (70%) / 7,500 Val (15%) / 7,500 Test (15%)** with 0 overlapping `image_id`, `rel_path`, or `md5_hash`.

## 2. Pixel, Lighting, Contrast & Sharpness Statistics (`fig03`, `fig04`)

| Metric (n=4,000 Stratified Sample) | Real Faces | AI-Generated Faces |
|---|---:|---:|
| **Mean Brightness (Luminance)** | `0.4583 ± 0.1092` | `0.4487 ± 0.1102` |
| **Mean Contrast (Luminance Std)** | `0.2250 ± 0.0479` | `0.2120 ± 0.0494` |
| **Median Sharpness (Laplacian Var)** | `0.008465` | `0.004592` |
| **Mean RGB Channels** | `[0.5463, 0.43, 0.373]` | `[0.5258, 0.4238, 0.3748]` |

- **Environmental Variation (`fig03`):** Real and synthetic faces span dark/high-key lighting, soft-focus blur vs. sharp detail, varying contrast, and warm/cool illumination casts — confirming that simple brightness/color heuristics alone cannot separate classes cleanly.

## 3. Frequency-Domain Forensics (`fig05`)
- High-frequency radial power (`radius 70–99 px`, mean `log(1 + |FFT|)`):
  - **Real:** `1.4877` | **All Fakes:** `1.2660` | **StyleGAN2:** `1.3910` | **Stable Diffusion:** `1.7784`
- Visible azimuthal and spectral roll-off differences between real camera portraits and GAN/Diffusion generators motivate our **Family 1 Traditional CV Baseline (`M1`: 2D FFT + LBP + Color → SVM/RF)** and our **Robustness Augmentation (`STEP-012`)**.

## 4. Preprocessing & Training-Only Augmentation Verification (`fig06`)
- Validation/test images undergo strictly deterministic `224×224` bicubic resizing and ImageNet normalization.
- Training-only robustness augmentations (horizontal flip, JPEG recompression `q=40–95`, Gaussian blur, color jitter) are verified visually in `fig06_augmentation_preview.png` and programmatically via `03_preprocessing/test_transforms.py`.
