# Split Verification Report — `DS0001` (`STEP-005`)

> **Seed:** `42` | **Policy:** Immutable, zero-leakage splits verified on `image_id`, `rel_path`, and `md5_hash`.

## 1. Canonical Stratified Split (`02_data/splits/ds0001_split_v1.csv`)

| Split | Total | Real (`0`) | Fake (`1`) | Fake Share | Unique MD5s |
|---|---:|---:|---:|---:|---:|
| `train` | 35,000 | 17,500 | 17,500 | 50.00% | 35,000 |
| `val` | 7,500 | 3,750 | 3,750 | 50.00% | 7,500 |
| `test` | 7,500 | 3,750 | 3,750 | 50.00% | 7,500 |
| **Total** | **50,000** | **25,000** | **25,000** | **50.00%** | **50,000** |

### Per-Generator Counts Across `ds0001_split_v1.csv`

| Generator | Train | Val | Test | Total |
|---|---:|---:|---:|---:|
| `cips` | 1,346 | 289 | 288 | 1,923 |
| `face_synthetics` | 1,346 | 288 | 289 | 1,923 |
| `gansformer` | 1,346 | 289 | 288 | 1,923 |
| `lama` | 1,346 | 288 | 289 | 1,923 |
| `mat` | 1,346 | 288 | 289 | 1,923 |
| `none` | 17,500 | 3,750 | 3,750 | 25,000 |
| `projected_gan` | 1,346 | 289 | 288 | 1,923 |
| `sfhq` | 1,346 | 288 | 289 | 1,923 |
| `stable_diffusion` | 1,346 | 288 | 289 | 1,923 |
| `stargan` | 1,346 | 289 | 288 | 1,923 |
| `stylegan1` | 1,346 | 289 | 288 | 1,923 |
| `stylegan2` | 1,347 | 289 | 288 | 1,924 |
| `stylegan3` | 1,347 | 288 | 288 | 1,923 |
| `taming_transformer` | 1,346 | 288 | 289 | 1,923 |

## 2. Unseen-Generator Ablation Split (`02_data/splits/ds0001_unseen_gen_split.csv`)

Held-out unseen test generators (0 samples in train/val): **`stable_diffusion`, `stylegan3`**.

| Split | Total | Real (`0`) | Fake (`1`) | Fake Generators Present |
|---|---:|---:|---:|---:|
| `train` | 35,961 | 17,980 | 17,981 | 11 |
| `val` | 6,347 | 3,174 | 3,173 | 11 |
| `test` | 7,692 | 3,846 | 3,846 | 2 |

## 3. Automated Zero-Leakage Assertions

- `train ∩ val == ∅`, `train ∩ test == ∅`, `val ∩ test == ∅` verified on `image_id`, `rel_path`, and `md5_hash`: **PASS**
- Class balance preserved at exact 50.00% / 50.00% across all splits: **PASS**
- Unseen generators (stable_diffusion, stylegan3) strictly absent from train/val in unseen-generator split: **PASS**
