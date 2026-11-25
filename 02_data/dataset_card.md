# Dataset Card — `DS0001`: ArtiFact Face Subset (`STEP-003`)

> **Project:** AI-Generated Face Detection for Digital Identity Verification (e-KYC) and Fraud Prevention (`GROUP 08`)  
> **Owner:** Member 1 — Md Assaduzzaman (`0242310005101233`)  
> **Storage Tier:** Kaggle Dataset (`kaggle:isthisdeception/ds0001-artifact-face-subset`) — raw image bytes are never committed to GitHub.  
> **License File:** [`02_data/DS0001_LICENSE.txt`](./DS0001_LICENSE.txt) (**MIT License**)  

---

## 1. Dataset Overview & Source Documentation

| Field | Value |
|---|---|
| **Dataset ID** | `DS0001` |
| **Canonical Name** | ArtiFact Face Subset (50k curated face subset of ArtiFact) |
| **Primary Citation** | Md Awsafur Rahman, Bishmoy Paul, Najibul Haque Sarker, Zaber Ibn Abdul Hakim, and Shaikh Anowarul Fattah, *"ArtiFact: A Large-Scale Dataset with Artificial and Factual Images for Generalizable and Robust Synthetic Image Detection"*, IEEE ICIP 2023 / OpenML 2023. |
| **Remote Storage Pointer** | `https://www.kaggle.com/datasets/isthisdeception/ds0001-artifact-face-subset` |
| **License & Usage Rights** | **MIT License** — permissive for academic research, modification, model training, and open-source educational applications with copyright notice retention. |
| **Total Images** | **50,000** face images |
| **Class Balance** | **25,000 Real (`0`)** / **25,000 AI-Generated Fake (`1`)** — exact `50.0% / 50.0%` balance |
| **Image Format & Mode** | JPEG (`RGB`, 3 channels) |
| **Spatial Dimensions** | `200 × 200` pixels (aspect ratio `1.00`, uniform cropped faces) |
| **Data Integrity** | `0` corrupt files, `0` empty files, `0` unsupported formats (independently re-verified via [`04_notebooks/01_ds0001_audit_and_index.ipynb`](../04_notebooks/01_ds0001_audit_and_index.ipynb)) |

---

## 2. Class & 13-Generator Breakdown

Unlike single-generator face datasets (e.g., StyleGAN-only 140k Faces), `DS0001` spans **13 distinct generative model families** covering GANs, Diffusion, Vision Transformers, Neural Inpainting, and 3D/Synthetic pipelines:

| Label (`int`) | `label_name` | Generator (`generator`) | Generative Paradigm | Image Count | Share (%) |
|---:|---|---|---|---:|---:|
| `0` | `real` | `none` | Real human photographs (FFHQ / CelebA-HQ lineage) | 25,000 | 50.00% |
| `1` | `fake` | `stylegan1` | Style-based GAN (v1) | 1,923 | 3.85% |
| `1` | `fake` | `stylegan2` | Style-based GAN (v2) | 1,924 | 3.85% |
| `1` | `fake` | `stylegan3` | Alias-free StyleGAN (v3) | 1,923 | 3.85% |
| `1` | `fake` | `stargan` | Multi-domain facial attribute GAN | 1,923 | 3.85% |
| `1` | `fake` | `projected_gan` | Feature-projected GAN | 1,923 | 3.85% |
| `1` | `fake` | `gansformer` | Bipartite Transformer-GAN hybrid | 1,923 | 3.85% |
| `1` | `fake` | `cips` | Conditionally-Independent Pixel Synthesis | 1,923 | 3.85% |
| `1` | `fake` | `sfhq` | Synthetic Faces High Quality | 1,923 | 3.85% |
| `1` | `fake` | `face_synthetics` | Procedural 3D graphics synthetic faces | 1,923 | 3.85% |
| `1` | `fake` | `stable_diffusion` | Latent Diffusion Model | 1,923 | 3.85% |
| `1` | `fake` | `taming_transformer` | VQGAN + Autoregressive Transformer | 1,923 | 3.85% |
| `1` | `fake` | `lama` | Large Mask Fourier-Convolution Inpainting | 1,923 | 3.85% |
| `1` | `fake` | `mat` | Mask-Aware Transformer Inpainting | 1,923 | 3.85% |
| **Total** | — | **14 groups (Real + 13 Fake)** | — | **50,000** | **100.00%** |

---

## 3. Annotation Schema & Example Index Records

The Kaggle audit notebook [`04_notebooks/01_ds0001_audit_and_index.ipynb`](../04_notebooks/01_ds0001_audit_and_index.ipynb) produces `02_data/ds0001_index.csv` with the following canonical schema:

| Column | Type | Description |
|---|---|---|
| `image_id` | `str` | Unique zero-padded identifier (`DS0001_000001` … `DS0001_050000`) |
| `rel_path` | `str` | Portable path relative to the Kaggle `DS0001` root (POSIX `/`) |
| `label` | `int` | Binary target: `0` = Real human face, `1` = AI-Generated face |
| `label_name` | `str` | Human-readable class (`real` / `fake`) |
| `generator` | `str` | Source generator name (`none` for real; one of 13 generators for fake) |
| `width` | `int` | Verified pixel width (`200`) |
| `height` | `int` | Verified pixel height (`200`) |
| `file_ext` | `str` | Lowercase file extension (`.jpg`) |
| `md5_hash` | `str` | 32-char MD5 checksum used in `STEP-005` to enforce zero split leakage |

### Schema Example (Illustrative Structure)

```csv
image_id,rel_path,label,label_name,generator,width,height,file_ext,md5_hash
DS0001_000001,real/00001.jpg,0,real,none,200,200,.jpg,<32-char-md5>
DS0001_025001,fake/00001.jpg,1,fake,stable_diffusion,200,200,.jpg,<32-char-md5>
DS0001_026924,fake/01924.jpg,1,fake,stylegan2,200,200,.jpg,<32-char-md5>
```

---

## 4. Relevance to Industry Problem (e-KYC Fraud Detection)

- **Multi-Generator Coverage:** Real-world e-KYC attackers do not rely on a single generator. Training on 13 diverse paradigms (GANs, Diffusion, Transformers, Inpainting, 3D graphics) prevents the detector from memorizing one generator's fingerprint.
- **Balanced Evaluation:** Equal real/fake class proportions allow clean accuracy, precision, recall, F1, and ROC-AUC comparisons, while generator tags enable **per-generator breakdown (`STEP-014`)** and **unseen-generator hold-out ablation (`STEP-013`)**.

---

## 5. Known Biases, Privacy/Safety & Practical Limitations

1. **Cropped-Face Domain:** All images are tightly cropped `200 × 200` faces. To prevent domain mismatch on real-world portraits or webcam captures, our deployed Streamlit app (`STEP-016`–`STEP-017`) incorporates an **automatic face detector and cropper** prior to inference.
2. **Real-Class Demographic Skew:** Real faces derive from public web/celebrity face corpora (FFHQ / CelebA-HQ lineage), which carry known demographic and lighting skews. This limitation is explicitly documented in Report Section 14 alongside future demographic fairness auditing.
3. **Compression & Post-Processing:** In real e-KYC pipelines, uploaded images undergo browser/mobile JPEG compression and slight blur. We mitigate this via **robustness-aware training-only augmentation (`STEP-012`)**.
4. **Privacy & Safety:** `DS0001` consists strictly of publicly released research imagery under MIT License. No private user records or biometric identification (face recognition) models are trained; the system strictly performs binary authenticity screening (`Real` vs. `AI-Generated`) and never stores uploaded user images during app inference.
