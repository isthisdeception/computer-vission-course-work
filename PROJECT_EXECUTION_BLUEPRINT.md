<!--
============================================================================
 PROJECT EXECUTION BLUEPRINT — COMPUTER VISION COURSE WORK (FALL 2026)
 Executable A–Z Implementation Manual (STEP-001 through STEP-020)
============================================================================
 Single Source of Truth:
   https://github.com/isthisdeception/computer-vission-course-work
 Dataset Tier (Kaggle):
   kaggle:isthisdeception/ds0001-artifact-face-subset (DS0001 — MIT License)
============================================================================
-->

# PROJECT EXECUTION BLUEPRINT

### A–Z Execution Playbook for Industry-Oriented End-to-End Computer Vision Application Development

| Field | Value |
|---|---|
| **Document Title** | `PROJECT_EXECUTION_BLUEPRINT.md` |
| **Course Deliverable** | Computer Vision Project-Based Assignment (**5 Marks**) & Presentation (**8 Marks**) — **Total: 13 Marks** |
| **Semester & Deadline** | Fall 2026 — **Final PDF Report Due: Monday, 14 December 2026** |
| **Group & Team Size** | **GROUP 08** — Exactly 5 Students (M1: Md Assaduzzaman `0242310005101233`, M2: Khadijatul Kobra Keya `0242310005101223`, M3: Mymuna Ibnat Priota `0242310005101804`, M4: Odito Al Nafiu `0242310005101253`, M5: Ishrat Jahan `0242310005101164`) |
| **Industry Domain** | **Cybersecurity / Finance & Banking** (e-KYC Synthetic Identity & AI-Generated Face Fraud Prevention) |
| **Dataset (Single Dataset)** | `DS0001` — ArtiFact Face Subset (`kaggle:isthisdeception/ds0001-artifact-face-subset`, 50,000 images, 25k Real / 25k Fake, 13 generators, MIT License) |
| **Total Steps** | **20 sequential steps** (`STEP-001` … `STEP-020`) across **7 Parts** |
| **Single Source of Truth** | GitHub (`https://github.com/isthisdeception/computer-vission-course-work`) |
| **Training Environment** | Kaggle GPU (T4 / P100) for DL training & evaluation; Local Python/Streamlit for working app demo |
| **AI Usage Policy** | **Strictly `< 25%` of substantive project work** + mandatory transparent AI Usage Declaration |

---

## How To Use This Blueprint

1. **Execute strictly in order (`STEP-001` → `STEP-020`).** Do not skip prerequisites. To run a step, simply pick the next `PENDING` step in [`PROGRESS_TRACKER.md`](./PROGRESS_TRACKER.md) (e.g., *"Execute STEP-001"*).
2. **GitHub is the single source of truth.** Every step ends with its code, CSV tables, figures, configs, and logs committed and pushed to `main` (or merged via PR) and [`PROGRESS_TRACKER.md`](./PROGRESS_TRACKER.md) updated.
3. **Never commit raw images or huge checkpoints to GitHub.** `DS0001` lives on Kaggle. Only metadata CSVs, split manifests, scripts, notebooks, metrics tables, lightweight visualizations, app code, and report assets are stored in Git.
4. **Every number must come from real experiments.** Zero fabricated results, zero guessed citations, zero unverified metrics. Every number in the report and slides must match a CSV/JSON file in `06_evaluation/`.
5. **Respect the `< 25%` AI Usage Policy & Team Ownership.** All 5 members must independently execute, validate, and understand their assigned work. Log every AI-assisted task honestly in `01_management/ai_usage_log.md`.
6. **Universal Definition of Done (DoD):** A step is `DONE` only when: (a) all Expected Outputs exist at exact paths, (b) Verification Checklist passes 100%, (c) `PROGRESS_TRACKER.md` is updated, and (d) changes are committed and pushed to GitHub.

---

## Legend

- **[H]** Human / Team Decision or Authoring Required
- **[K]** Executed on Kaggle GPU / Notebook
- **[L]** Executed Locally (Python / Streamlit / Report Build)
- **[M1]–[M5]** Primary Responsible Team Member (Member 1 … Member 5)

---

## Assignment Rubric Coverage Map

| Assignment Rubric Section | Marks | Covered By Steps |
|---|---|---|
| **Part A.1:** Industry problem identification & visual dataset analysis | 0.75 | `STEP-001`, `STEP-003`, `STEP-004` |
| **Part A.2:** Image preprocessing, augmentation & leak-free data splits | 0.75 | `STEP-005`, `STEP-006` |
| **Part A.3:** Vision models (≥4 models, ≥2 families), optimization (≥3), ablation & evaluation | 1.25 | `STEP-007` – `STEP-015` |
| **Part A.4:** Working vision application & industry relevance | 0.75 | `STEP-016` – `STEP-018` |
| **Part A.5:** Report quality (17 mandatory sections), documentation & reproducibility | 1.00 | `STEP-002`, `STEP-019` |
| **Part A.6:** Individual contributions (5 members) & AI usage compliance (<25%) | 0.50 | `STEP-001`, `STEP-019`, `STEP-020` |
| **Part B:** In-class Presentation (10 topics, 5-ID footer on every slide, live demo) | 8.00 | `STEP-018`, `STEP-020` |

---

## End-to-End Dependency Flow

```text
PART 1: Governance & Repo Bootstrap (STEP-001 – STEP-002)         ──► [GATE 1]
PART 2: DS0001 Audit, Visual EDA, Splits & Aug (STEP-003 – 006)   ──► [GATE 2]
PART 3: 4 Vision Models / 3 Families (STEP-007 – STEP-010)        ──► [GATE 3]
PART 4: 3 Optimizations + Controlled Ablation (STEP-011 – 013)
PART 5: Test Metrics, Per-Gen, XAI & Errors (STEP-014 – 015)      ──► [GATE 4]
PART 6: Working Streamlit e-KYC Vision App (STEP-016 – 018)       ──► [GATE 5]
PART 7: 17-Section PDF Report & Presentation (STEP-019 – 020)     ──► [GATE 6 — SUBMIT DEC 14]
```

---

## Locked Dataset Reference (`DS0001`)

| Property | Exact Specification |
|---|---|
| **Dataset ID & Name** | `DS0001` — ArtiFact Face Subset (Rahman et al., 2023) |
| **Kaggle Slug** | `kaggle:isthisdeception/ds0001-artifact-face-subset` |
| **License** | MIT License (public, permissive) |
| **Total Images** | 50,000 face images (0 corrupt) |
| **Class Balance** | 25,000 Real (`none`) / 25,000 Fake (50.0% / 50.0%) |
| **13 Synthetic Generators** | `stylegan1` (1,923), `stylegan2` (1,924), `stylegan3` (1,923), `stargan` (1,923), `projected_gan` (1,923), `gansformer` (1,923), `cips` (1,923), `sfhq` (1,923), `face_synthetics` (1,923), `stable_diffusion` (1,923), `taming_transformer` (1,923), `lama` (1,923), `mat` (1,923) |
| **Resolution / Format** | Cropped faces (~200×200), PNG/JPG |
| **Live-Demo Implication** | Because training images are cropped faces, the deployed app (`STEP-016`–`STEP-017`) **must** include an automatic face detector & cropper before inference. |

---

# PART 1 — GOVERNANCE, SCOPE & REPOSITORY BOOTSTRAP

> Establishes the 5-member team charter, industry problem framing, repository skeleton, registries, environment pins, and `< 25%` AI usage tracking.

---

## STEP-001 — Team Charter, Industry Problem Definition & Scope Lock  **[H][M1][All]**

**Title:** Lock the 5 team members, industry problem statement, objectives, and contribution plan.

**Objective:** Finalize all 5 students' full names and IDs, define the Cybersecurity / Finance e-KYC industry problem, stakeholders, measurable outcomes, and individual responsibility split.

**Rubric Mapping:** Section 1 (Objective), Section 2 (Industry Domains), Section 4 (Team Member Contributions), Section 5 (AI Usage Policy), Report Sections 1, 3, 15, 16.

**Prerequisites:** None.
**Estimated Time:** 1 hour.
**Parallelizable:** No.

**Inputs:** Assignment guidelines; all 5 team members' full names & student IDs.

**Expected Outputs:**
- `01_management/team_charter.md` — Team roster (5 full names + full student IDs + group number), industry problem statement, intended users/stakeholders (banks, fintech e-KYC teams, trust & safety analysts), expected industry benefits, measurable KPIs (e.g., ≥92% F1, low False Acceptance Rate on synthetic faces, <150 ms CPU inference).
- `01_management/team_contributions.csv` — Canonical tracking table (`member_no,name,student_id,responsibilities,planned_pct,actual_pct,verified_deliverables`).
- `01_management/ai_usage_log.md` — Template & live log tracking every AI tool used, purpose, affected section, and estimated % (strictly `< 25%`).
- `README.md` updated with actual team names and full student IDs.

**Execution Instructions:**
1. Collect all 5 full names, full student IDs, course code/section, and group number.
2. Confirm role ownership matching Assignment Section 4:
   - **M1:** Industry problem, `DS0001` dataset & license review, leak-free splits
   - **M2:** Visual EDA, preprocessing & training-only augmentation
   - **M3:** 4 vision model architectures across 3 families & baseline experiments
   - **M4:** 3 optimizations, ablation study, evaluation metrics, Grad-CAM/FFT & error analysis
   - **M5:** Working Streamlit vision application, face-crop pipeline, testing & integration
3. Write `01_management/team_charter.md` answering all 5 mandatory bullets of Assignment Section 2 (problem significance, stakeholders, proposed CV solution, measurable outcomes, practical application).

**GitHub Expectations:** Commit `docs(step-001): lock team charter, industry problem, and contribution plan` → push to `main`.

**Verification Checklist:**
- [ ] Exactly 5 students listed with full names & full student IDs.
- [ ] Industry problem explains real-world practical use (not just model benchmarking).
- [ ] Contribution percentages sum to 100%.
- [ ] `ai_usage_log.md` initialized with `< 25%` policy cap.

---

## STEP-002 — Repository Skeleton, Registries & Environment Lock  **[L][M5][All]**

**Title:** Create canonical folder structure, experiment/model registries, and pinned Python dependencies.

**Objective:** Bootstrap all 9 canonical directories (`01_management/` … `09_presentation/`), initialize CSV registries (`experiments.csv`, `models.csv`, `figures.csv`), and lock `requirements.txt` for Kaggle + local Streamlit reproducibility.

**Rubric Mapping:** Report Quality, Technical Documentation & Reproducibility (1.00 Mark).

**Prerequisites:** `STEP-001` complete.
**Estimated Time:** 1 hour.
**Parallelizable:** No.

**Inputs:** `PROJECT_EXECUTION_BLUEPRINT.md`, `.gitignore`.

**Expected Outputs:**
- Canonical directories with `.gitkeep` / short `README.md`:
  `01_management/`, `02_data/`, `03_preprocessing/`, `04_notebooks/`, `05_models/`, `06_evaluation/`, `07_app/`, `08_report/`, `09_presentation/`
- `05_models/experiment_registry.csv` (`exp_id,step_id,model_name,family,pretrained,resolution,augmentation,optimizer,lr,epochs,batch_size,val_acc,val_f1,val_auc,test_acc,test_f1,test_auc,notes`)
- `06_evaluation/figure_registry.csv` (`fig_id,filename,step_id,report_section,caption,source_script`)
- `requirements.txt` (PyTorch, torchvision, timm, scikit-learn, scikit-image, opencv-python-headless, mediapipe/facenet-pytorch or opencv DNN, pytorch-grad-cam, matplotlib, seaborn, pandas, numpy, Pillow, streamlit)
- `src/__init__.py` and `src/seed.py` (global deterministic seed helper `SEED=42`).

**GitHub Expectations:** Commit `chore(step-002): bootstrap repo skeleton, registries, and requirements` → push to `main`.

**Verification Checklist:**
- [ ] All 9 folders exist and follow exact naming.
- [ ] `git check-ignore` blocks `02_data/raw/test.jpg`, `model.pth`, `.env`, `kaggle.json`.
- [ ] **GATE 1 PASS:** `PROGRESS_TRACKER.md` updated for `STEP-001` and `STEP-002`.

---

# PART 2 — DATASET AUDIT, VISUAL EDA, LEAK-FREE SPLITS & PREPROCESSING

> Satisfies Assignment Sections **3A (Visual Dataset & Exploratory Analysis)** and **3B (Image Preprocessing & Augmentation)** using `DS0001`.

---

## STEP-003 — Kaggle `DS0001` Verification, License Documentation & Master Index CSV  **[K][M1]**

**Title:** Verify `DS0001` on Kaggle, document source/license, and generate a clean master metadata index.

**Objective:** Attach `isthisdeception/ds0001-artifact-face-subset` in a Kaggle notebook, enumerate all 50,000 images, verify readability (0 corrupt), compute MD5/perceptual hashes for duplicate checking, and export a lightweight `ds0001_index.csv` (no image bytes) to GitHub.

**Rubric Mapping:** Section 3A (clearly documented source & usage rights, image count, classes, label quality), Report Section 6.

**Prerequisites:** `STEP-002` complete.
**Estimated Time:** 1–2 hours.
**Parallelizable:** No.

**Inputs:** Kaggle dataset `isthisdeception/ds0001-artifact-face-subset`.

**Expected Outputs:**
- `04_notebooks/01_ds0001_audit_and_index.ipynb`
- `02_data/dataset_card.md` (source, citation Rahman et al. 2023, MIT license, privacy/ethics, class & generator counts, known limitations)
- `02_data/DS0001_LICENSE.txt` (MIT License text)
- `02_data/ds0001_audit_summary.json` (total scanned, readable count, corrupt count, exact duplicate hash count, width/height summary, color mode summary)
- `02_data/ds0001_index.csv` (`image_id,rel_path,label,label_name,generator,width,height,file_ext,md5_hash`)

**GitHub Expectations:** Commit `data(step-003): verify DS0001 on Kaggle and save master index + license` → push to `main`.

**Verification Checklist:**
- [ ] Exactly 50,000 images accounted for (25k real / 25k fake, 13 generators).
- [ ] Zero corrupt files confirmed; any exact duplicate hashes flagged for leak-free splitting in `STEP-005`.
- [ ] No raw images committed to GitHub.

---

## STEP-004 — Visual EDA: Distributions, Image Characteristics & Sample Grids  **[K][M2]**

**Title:** Perform comprehensive visual and statistical Exploratory Data Analysis on `DS0001`.

**Objective:** Produce publication-quality EDA plots and tables analyzing class balance, generator distribution, image dimensions, RGB/brightness/contrast distributions, sharpness/blur (Laplacian variance), frequency-domain (2D FFT) signatures, and visual sample grids showing environmental variations (lighting, viewpoint, blur, occlusion).

**Rubric Mapping:** Section 3A (dimensions, class balance, sample images, lighting/viewpoint/blur/occlusion), Report Section 7, Presentation Topic 3.

**Prerequisites:** `STEP-003` complete.
**Estimated Time:** 2–3 hours.
**Parallelizable:** Can run alongside `STEP-005` once `ds0001_index.csv` exists.

**Inputs:** `02_data/ds0001_index.csv` + Kaggle `DS0001`.

**Expected Outputs:**
- `04_notebooks/02_visual_eda.ipynb`
- `02_data/eda_summary.json` & `02_data/eda_generator_counts.csv`
- Figures saved in `06_evaluation/figures/eda/`:
  - `fig01_class_generator_distribution.png` (Real vs. Fake + 13 generator bar chart)
  - `fig02_sample_grid_real_vs_fake.png` (4×4 grid: real faces + diverse generator fakes labeled clearly)
  - `fig03_environmental_variations.png` (annotated examples of lighting, pose/viewpoint, blur, occlusion/glasses)
  - `fig04_pixel_brightness_blur_stats.png` (brightness, contrast, RGB histograms, Laplacian blur score: Real vs. Fake)
  - `fig05_average_fft_spectrum.png` (mean 2D FFT log-magnitude spectrum: Real vs. GAN vs. Diffusion — shows why frequency features work!)
- `02_data/eda_report.md` (concise analytical commentary of every plot).

**GitHub Expectations:** Commit `eda(step-004): complete visual EDA and generate figures fig01-fig05` → push to `main`.

**Verification Checklist:**
- [ ] All 5 EDA figures are crisp (≥300 DPI), readable, and registered in `06_evaluation/figure_registry.csv`.
- [ ] Environmental variations (lighting, viewpoint, blur, occlusion) explicitly analyzed with real samples.

---

## STEP-005 — Leak-Free Stratified Train/Val/Test Split (70/15/15)  **[K/L][M1][M2]**

**Title:** Create and verify an immutable, zero-leakage stratified dataset split.

**Objective:** Split `DS0001` into **70% Train (35,000) / 15% Val (7,500) / 15% Test (7,500)** stratified jointly by `(label, generator)` while grouping any identical `md5_hash` / subject IDs into the same split so **zero leakage** can occur across Train/Val/Test. Also define an optional **Unseen-Generator Split** (`split_unseen_gen.csv`) for the `STEP-013` ablation.

**Rubric Mapping:** Section 3B (train/val/test splits preventing data leakage between related images/subjects), Report Section 6.

**Prerequisites:** `STEP-003` complete.
**Estimated Time:** 1–2 hours.
**Parallelizable:** Yes (with `STEP-004`).

**Inputs:** `02_data/ds0001_index.csv`.

**Expected Outputs:**
- `03_preprocessing/create_splits.py` (deterministic, `SEED=42`)
- `02_data/splits/ds0001_split_v1.csv` (`image_id,rel_path,label,generator,split` where `split in {train,val,test}`)
- `02_data/splits/ds0001_unseen_gen_split.csv` (holds out 2 distinct generators, e.g., `stable_diffusion` + `stylegan3`, plus matched reals exclusively in test — used for generalization ablation in `STEP-013`)
- `02_data/splits/split_verification_report.md` (exact counts per split, per class, per generator, plus automated assertions proving `0` hash overlap and `0` path overlap).

**GitHub Expectations:** Commit `data(step-005): lock leak-free 70-15-15 stratified splits` → push to `main`.

**Verification Checklist:**
- [ ] `train ∩ val == ∅`, `train ∩ test == ∅`, `val ∩ test == ∅` (both by path and by `md5_hash`).
- [ ] Every split preserves ~50/50 Real/Fake balance and proportional representation across all 13 generators.
- [ ] Split CSVs are frozen — never altered after `STEP-005`.

---

## STEP-006 — Preprocessing & Training-Only Augmentation Pipeline  **[L/K][M2]**

**Title:** Implement reusable preprocessing and strictly training-only augmentation transforms.

**Objective:** Build clean PyTorch/Albumentations transform pipelines (`baseline_aug` and `robust_aug`) with resizing (224×224), RGB/YCbCr handling, ImageNet normalization, and **strictly training-only augmentations** (never applied to validation or test sets), plus a visual verification grid of augmented images.

**Rubric Mapping:** Section 3B (resizing, color-space, normalization, denoising/cropping, training-only augmentation), Report Section 8, Presentation Topic 4.

**Prerequisites:** `STEP-005` complete.
**Estimated Time:** 1–2 hours.
**Parallelizable:** No.

**Inputs:** `02_data/splits/ds0001_split_v1.csv`.

**Expected Outputs:**
- `03_preprocessing/transforms.py`:
  - `get_eval_transforms(img_size=224)` — Resize + ToTensor + Normalize (deterministic, zero randomness)
  - `get_train_transforms_basic(img_size=224)` — Resize + RandomHorizontalFlip + Normalize (used in Part 3 baseline models)
  - `get_train_transforms_robust(img_size=224)` — Resize + RandomHorizontalFlip + RandomJPEGCompression(q=40–95) + RandomGaussianBlur + ColorJitter + Normalize (used in `STEP-012` optimization & ablation)
- `03_preprocessing/dataset.py` — PyTorch `Dataset` + `DataLoader` factory reading `ds0001_split_v1.csv`
- `06_evaluation/figures/eda/fig06_augmentation_preview.png` (original image vs. 5 training-only augmented variants)
- `03_preprocessing/test_transforms.py` (unit test confirming val/test transforms are deterministic and never mutate labels).

**GitHub Expectations:** Commit `feat(step-006): add preprocessing and training-only augmentation pipeline` → push to `main`.

**Verification Checklist:**
- [ ] Unit test confirms identical output on repeated calls to `get_eval_transforms`.
- [ ] `fig06_augmentation_preview.png` saved and registered.
- [ ] **GATE 2 PASS:** All Part 2 deliverables verified and pushed; ready for model training.

---

# PART 3 — COMPUTER VISION MODEL DEVELOPMENT (4 MODELS, 3 FAMILIES)

> Satisfies Assignment Section **3C**: implement & compare **≥4 meaningful models** across **≥2 distinct methodological families**, include **≥1 deep learning model**, and clearly separate pre-trained weights vs. team fine-tuning.

| Model ID | Model / Pipeline | Family | Pre-Trained Weights & Role |
|---|---|---|---|
| **M1** | **2D FFT Radial Spectrum + LBP + Color Stats → Random Forest / Linear SVM** | **Family 1: Traditional Image Processing / Handcrafted Features** | None (trained from scratch) — interpretable non-DL baseline |
| **M2** | **ResNet-50** (`M2a`: Frozen linear probe vs. `M2b`: Fine-tuned) | **Family 2: Classic CNN** | ImageNet-1K pre-trained — explicitly contrasts frozen pre-trained features vs. team fine-tuning |
| **M3** | **EfficientNet-B0** (Fine-tuned) | **Family 2: Lightweight / Efficient CNN** | ImageNet-1K pre-trained — industry-oriented low-latency architecture |
| **M4** | **ViT-B/16** (or **Swin-Tiny**, Fine-tuned) | **Family 3: Vision Transformer** | ImageNet-1K pre-trained — global self-attention vs. local CNN comparison |

---

## STEP-007 — Model 1 (Traditional CV Baseline): FFT + LBP + Color Features → SVM / Random Forest  **[K][M3]**

**Title:** Build and evaluate the traditional handcrafted computer vision baseline (`M1`).

**Objective:** Extract classic forensic/texture features — 2D FFT azimuthal radial power spectrum (frequency artifacts), Local Binary Patterns (LBP micro-texture), and YCbCr color channel statistics — and train **Random Forest** and **RBF/Linear SVM** classifiers on `ds0001_split_v1.csv`.

**Rubric Mapping:** Section 3C (distinct traditional image-processing/feature-based family vs. deep learning; clear baseline), Report Section 9.

**Prerequisites:** `STEP-006` complete.
**Estimated Time:** 2–3 hours.
**Parallelizable:** Yes (independent of M2–M4).

**Inputs:** `02_data/splits/ds0001_split_v1.csv`, Kaggle `DS0001`.

**Expected Outputs:**
- `04_notebooks/03_model1_traditional_cv_baseline.ipynb`
- `05_models/traditional_features.py` (reusable feature extractor)
- `06_evaluation/metrics/M1_traditional_metrics.json` (Val & Test Accuracy, Precision, Recall, F1, ROC-AUC, inference time ms/image)
- `06_evaluation/figures/models/fig07_m1_feature_importance.png` (top frequency/texture features separating Real vs. AI)
- `05_models/experiment_registry.csv` updated with `EXP-M1`.

**Execution Note:** Extracting FFT+LBP on all 50k images takes ~5–10 min with multiprocessing on Kaggle CPU. If using a stratified subset (e.g., 15k train / 5k val / 7.5k test) for SVM speed, document the exact subset size transparently and keep the **exact same 7,500 test set** for fair comparison across all 4 models.

**GitHub Expectations:** Commit `exp(step-007): implement and evaluate M1 traditional CV baseline (FFT+LBP)` → push to `main`.

**Verification Checklist:**
- [ ] Feature extractor fit (`StandardScaler`) is fitted **strictly on Train split only** (zero leakage).
- [ ] Evaluated on the full canonical `test` split (7,500 images).
- [ ] Metrics logged in `experiment_registry.csv`.

---

## STEP-008 — Model 2 (CNN): ResNet-50 — Frozen Pre-Trained Baseline vs. Fine-Tuned  **[K][M3]**

**Title:** Train ResNet-50 in two modes (`M2a` frozen backbone vs. `M2b` full fine-tuning).

**Objective:** Explicitly satisfy the rubric requirement to *"explain any use of pre-trained weights and distinguish baseline performance from the team's own training or fine-tuning"* by evaluating ImageNet-pretrained **ResNet-50** first with a frozen backbone (linear head only, `M2a`) and then fine-tuning all layers (`M2b`) using `basic` training augmentation.

**Rubric Mapping:** Section 3C (deep learning CNN + pre-trained baseline vs. team fine-tuning), Report Section 9.

**Prerequisites:** `STEP-006` complete.
**Estimated Time:** 2–3 hours on Kaggle GPU.
**Parallelizable:** Yes (with M1, M3, M4).

**Inputs:** `02_data/splits/ds0001_split_v1.csv`, `03_preprocessing/transforms.py`.

**Expected Outputs:**
- `04_notebooks/04_model2_resnet50.ipynb`
- `06_evaluation/metrics/M2a_resnet50_frozen_metrics.json` & `M2b_resnet50_finetuned_metrics.json`
- `06_evaluation/curves/M2_resnet50_history.csv` (epoch-by-epoch train/val loss, acc, F1)
- `05_models/experiment_registry.csv` updated (`EXP-M2a`, `EXP-M2b`); best checkpoint saved on Kaggle Output.

**GitHub Expectations:** Commit `exp(step-008): train M2 ResNet-50 frozen vs fine-tuned baseline` → push to `main`.

**Verification Checklist:**
- [ ] Clear quantitative gap documented between `M2a` (frozen pre-trained) and `M2b` (team fine-tuned).
- [ ] Mixed precision (`torch.cuda.amp`) + early stopping used; best checkpoint selected by Validation F1/AUC only (never Test).

---

## STEP-009 — Model 3 (Efficient Industry CNN): EfficientNet-B0  **[K][M3]**

**Title:** Fine-tune EfficientNet-B0 for high-efficiency industry deployment (`M3`).

**Objective:** Train **EfficientNet-B0** (ImageNet-1K pretrained, fine-tuned on `DS0001`) under the exact same baseline protocol as `M2b` to benchmark a compact, fast-inference architecture suitable for real-time e-KYC servers.

**Rubric Mapping:** Section 3C (4 meaningful models, practical industry trade-off), Report Section 9.

**Prerequisites:** `STEP-006` complete.
**Estimated Time:** 2 hours on Kaggle GPU.
**Parallelizable:** Yes (with M1, M2, M4).

**Inputs:** `02_data/splits/ds0001_split_v1.csv`, `03_preprocessing/transforms.py`.

**Expected Outputs:**
- `04_notebooks/05_model3_efficientnet_b0.ipynb`
- `06_evaluation/metrics/M3_efficientnet_b0_metrics.json`
- `06_evaluation/curves/M3_efficientnet_b0_history.csv`
- `05_models/experiment_registry.csv` updated (`EXP-M3`); best checkpoint saved on Kaggle Output.

**GitHub Expectations:** Commit `exp(step-009): train M3 EfficientNet-B0 baseline` → push to `main`.

**Verification Checklist:**
- [ ] Identical split (`ds0001_split_v1.csv`), seed (`42`), and baseline augmentation as `M2b`.
- [ ] Parameter count and model size (MB) recorded alongside Val/Test metrics.

---

## STEP-010 — Model 4 (Vision Transformer): ViT-B/16 & 4-Model Baseline Comparison  **[K][M3]**

**Title:** Fine-tune Vision Transformer (`ViT-B/16` or `Swin-Tiny`) and synthesize the 4-model baseline comparison.

**Objective:** Train **ViT-B/16** (or **Swin-Tiny** via `timm`, ImageNet-1K pretrained) as Family 3 (Transformer), then generate a unified 4-model baseline comparison table and training-curve plots to select the top candidate(s) for Part 4 optimization.

**Rubric Mapping:** Section 3C (≥4 models across ≥2 families; CNN vs. ViT vs. Traditional CV), Report Sections 9 & 11.

**Prerequisites:** `STEP-007`, `STEP-008`, `STEP-009` complete.
**Estimated Time:** 2–3 hours on Kaggle GPU.
**Parallelizable:** No (aggregates M1–M4).

**Inputs:** M1–M3 metrics + Kaggle `DS0001`.

**Expected Outputs:**
- `04_notebooks/06_model4_vit_and_baseline_comparison.ipynb`
- `06_evaluation/metrics/M4_vit_metrics.json` & `06_evaluation/curves/M4_vit_history.csv`
- `06_evaluation/tables/table01_baseline_4model_comparison.csv` (M1, M2a, M2b, M3, M4 — Params, Size MB, Val F1, Test Acc, Test Precision, Test Recall, Test F1, Test ROC-AUC)
- `06_evaluation/figures/models/fig08_baseline_model_comparison.png` (grouped bar chart + learning curves)
- `05_models/experiment_registry.csv` updated (`EXP-M4`).

**GitHub Expectations:** Commit `exp(step-010): train M4 ViT and compile 4-model baseline comparison` → push to `main`.

**Verification Checklist:**
- [ ] All 4 models across 3 distinct families compared on the exact same canonical test split.
- [ ] **GATE 3 PASS:** Top 2–3 models identified for Part 4 optimization; `PROGRESS_TRACKER.md` updated.

---

# PART 4 — OPTIMIZATION & CONTROLLED ABLATION EXPERIMENTS

> Satisfies Assignment Section **3D**: optimize **at least 3 selected model configurations or training strategies** with clear **before/after** results, plus **at least 1 justified controlled ablation**.

---

## STEP-011 — Optimization 1: Optimizer, Learning Rate Schedule & Layer-Wise Regularization  **[K][M4]**

**Title:** Optimize training dynamics (`Adam` fixed LR → `AdamW` + `CosineAnnealingLR` + Label Smoothing / Weight Decay).

**Objective:** Take the top-performing model(s) from `STEP-010` (e.g., `M3 EfficientNet-B0` and/or `M4 ViT` / `M2b ResNet-50`) and run a controlled before/after optimization comparing default `Adam (lr=1e-3)` vs. `AdamW (lr=1e-4, weight_decay=1e-2)` + linear warmup + `CosineAnnealingLR` + `label_smoothing=0.05`.

**Rubric Mapping:** Section 3D (Optimization 1: optimizer, LR, regularization — before/after report), Report Section 10.

**Prerequisites:** `STEP-010` complete.
**Estimated Time:** 2–3 hours on Kaggle GPU.
**Parallelizable:** Can run sequentially with `STEP-012` / `STEP-013`.

**Inputs:** Top baseline checkpoint configs from Part 3.

**Expected Outputs:**
- `04_notebooks/07_optimizations_and_ablation.ipynb` (Section 1: OPT-1)
- `06_evaluation/metrics/OPT1_optimizer_lr_comparison.json`
- `06_evaluation/tables/table02_optimization_before_after.csv` (started with OPT-1 rows)
- `05_models/experiment_registry.csv` updated (`EXP-OPT1`).

**GitHub Expectations:** Commit `exp(step-011): run OPT-1 optimizer and cosine LR schedule tuning` → push to `main`.

**Verification Checklist:**
- [ ] Only optimizer/LR/regularization changed while keeping data split and augmentation identical (clean before/after comparison).
- [ ] Exact before/after Val F1, Test F1, and ROC-AUC logged.

---

## STEP-012 — Optimization 2: Robustness-Aware Training Augmentation (JPEG + Blur + Color Jitter)  **[K][M4]**

**Title:** Optimize real-world robustness via training-only social-media / camera degradation augmentation.

**Objective:** Train the best architecture using `get_train_transforms_robust()` (JPEG compression q=40–95, Gaussian blur, color jitter, random flip) and compare **before vs. after** on both: (a) the **clean** canonical test set, and (b) a **degraded** copy of the test set (JPEG q=60 + mild blur simulating WhatsApp/web e-KYC uploads).

**Rubric Mapping:** Section 3D (Optimization 2: augmentation strategy — before/after), real-world industry robustness, Report Section 10.

**Prerequisites:** `STEP-011` complete.
**Estimated Time:** 2–3 hours on Kaggle GPU.
**Parallelizable:** No (builds on OPT-1 settings).

**Inputs:** `03_preprocessing/transforms.py`, `OPT-1` best config.

**Expected Outputs:**
- `04_notebooks/07_optimizations_and_ablation.ipynb` (Section 2: OPT-2)
- `06_evaluation/metrics/OPT2_robust_aug_comparison.json` (clean test vs. degraded test: before vs. after)
- `06_evaluation/figures/models/fig09_robustness_before_after.png` (bar chart showing accuracy/F1 retention under JPEG/blur compression!)
- `06_evaluation/tables/table02_optimization_before_after.csv` updated with OPT-2 rows; `experiment_registry.csv` updated (`EXP-OPT2`).

**GitHub Expectations:** Commit `exp(step-012): run OPT-2 robustness augmentation and degradation test` → push to `main`.

**Verification Checklist:**
- [ ] Augmentation applied strictly to Training set only.
- [ ] Both clean and degraded test performance clearly reported before/after.

---

## STEP-013 — Optimization 3 (Threshold Calibration / Resolution) & Controlled Ablation Study  **[K][M4]**

**Title:** Calibrate decision threshold for e-KYC risk control (`OPT-3`) and run a justified controlled ablation (`ABL-1`).

**Objective:**
1. **OPT-3 (Threshold & Resolution/Architecture Strategy):** Optimize the decision threshold on the **Validation set** (comparing default `0.50` vs. optimal F1 threshold vs. e-KYC low-FPR operating point at `FPR ≤ 2%`), AND/OR compare input resolution (`200×200` native vs. `224×224` / `256×256` or two-stage progressive unfreezing) — reporting exact before/after metrics on Test.
2. **ABL-1 (Controlled Ablation):** Conduct at least one justified controlled ablation:
   - **Ablation A (Recommended):** *With vs. Without Robustness Augmentation* across clean vs. compressed test conditions (quantifying exact robustness gain), **and/or**
   - **Ablation B (High-Impact Generalization):** *Unseen-Generator Hold-Out Ablation* using `ds0001_unseen_gen_split.csv` (train on 11 generators, evaluate on 2 completely unseen generators — `stable_diffusion` + `stylegan3`) to quantify real-world generalization gap!

**Rubric Mapping:** Section 3D (3rd optimization + justified controlled ablation), Report Section 10.

**Prerequisites:** `STEP-012` complete.
**Estimated Time:** 2–3 hours on Kaggle GPU.
**Parallelizable:** No.

**Inputs:** `OPT-2` model probabilities on Val/Test + `ds0001_unseen_gen_split.csv`.

**Expected Outputs:**
- `04_notebooks/07_optimizations_and_ablation.ipynb` (Sections 3 & 4: OPT-3 + ABL-1)
- `06_evaluation/metrics/OPT3_threshold_and_ablation.json`
- `06_evaluation/tables/table02_optimization_before_after.csv` (finalized with all 3 optimizations)
- `06_evaluation/tables/table03_ablation_results.csv`
- `06_evaluation/figures/models/fig10_threshold_pr_roc_curve.png` (ROC & PR curves with calibrated e-KYC operating point marked)
- `05_models/experiment_registry.csv` updated (`EXP-OPT3`, `EXP-ABL1`).

**GitHub Expectations:** Commit `exp(step-013): complete OPT-3 threshold calibration and controlled ablation` → push to `main`.

**Verification Checklist:**
- [ ] Threshold selected strictly on Validation set, then applied unchanged to Test set (no test leakage!).
- [ ] At least 3 distinct optimizations + 1 controlled ablation cleanly tabulated.

---

# PART 5 — TASK-SPECIFIC EVALUATION, EXPLAINABILITY & ERROR ANALYSIS

> Satisfies Assignment Section **3E**: classification metrics, confusion matrix, qualitative outputs, failure-case analysis, Grad-CAM/saliency/FFT visualizations, inference speed, practical limitations, and final model selection rationale.

---

## STEP-014 — Final Test Evaluation, Per-Generator Breakdown & Inference Speed Benchmark  **[K/L][M4]**

**Title:** Run comprehensive quantitative evaluation across all models, all 13 generators, and hardware latency.

**Objective:** Produce the final frozen evaluation suite on the canonical 7,500-image Test set: Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrices, **13-generator accuracy breakdown**, and **inference speed (ms/image)** on both Kaggle GPU and local CPU (critical for e-KYC deployment feasibility).

**Rubric Mapping:** Section 3E (metrics, confusion matrix, inference speed), Report Section 11, Presentation Topic 6.

**Prerequisites:** `STEP-013` complete.
**Estimated Time:** 2 hours.
**Parallelizable:** Can overlap with `STEP-015`.

**Inputs:** Final optimized model checkpoints + baseline predictions.

**Expected Outputs:**
- `04_notebooks/08_final_evaluation_and_xai.ipynb` (Part 1: Quantitative Metrics)
- `06_evaluation/tables/table04_final_model_comparison.csv` (all 4 baseline models + final optimized model: Acc, Prec, Rec, F1, AUC, Params, Model MB, GPU ms/img, CPU ms/img)
- `06_evaluation/tables/table05_per_generator_accuracy.csv` (Recall / detection rate across all 13 synthetic generators + Real specificity)
- `06_evaluation/figures/eval/fig11_confusion_matrices.png` (side-by-side normalized + raw confusion matrices: M1 vs. Best Final Model)
- `06_evaluation/figures/eval/fig12_per_generator_performance.png` (horizontal bar chart across all 13 generators).

**GitHub Expectations:** Commit `eval(step-014): generate final metrics, per-generator table, and latency benchmark` → push to `main`.

**Verification Checklist:**
- [ ] Every metric matches exact JSON/CSV logs — zero manual typos.
- [ ] Both GPU and CPU inference latency (averaged over ≥100 images after warmup) documented.

---

## STEP-015 — Explainability (Grad-CAM + FFT), Failure-Case Analysis & Final Model Selection  **[K][M4]**

**Title:** Generate Grad-CAM & frequency visualizations, analyze failure modes, and formally select the final deployment model.

**Objective:** Produce qualitative prediction panels, **Grad-CAM** overlays (highlighting eye, skin texture, hairline, and background artifact regions), **2D FFT spectrum** comparisons, and a structured **Failure-Case Analysis** (False Positives + False Negatives with root-cause categorization), followed by a written justification for selecting the final production model.

**Rubric Mapping:** Section 3E (qualitative outputs, failure-case analysis, Grad-CAM/saliency visualizations, model selection justification, practical limitations), Report Section 12, Presentation Topic 7.

**Prerequisites:** `STEP-014` complete.
**Estimated Time:** 2–3 hours.
**Parallelizable:** No.

**Inputs:** Final optimized model + test predictions (`y_true`, `y_pred`, `y_prob`, `generator`).

**Expected Outputs:**
- `04_notebooks/08_final_evaluation_and_xai.ipynb` (Part 2: Grad-CAM, FFT & Error Analysis)
- `06_evaluation/figures/xai/fig13_gradcam_correct_predictions.png` (4 Real + 4 AI-Generated faces with original, Grad-CAM overlay, predicted label & confidence)
- `06_evaluation/figures/xai/fig14_failure_cases_fp_fn.png` (4 False Positives + 4 False Negatives with Grad-CAM + root-cause notes: e.g., heavy blur, extreme lighting, realistic diffusion skin)
- `06_evaluation/figures/xai/fig15_fft_real_vs_fake_cases.png` (side-by-side 2D FFT spectrum of sample Real vs. GAN vs. Diffusion images)
- `06_evaluation/model_selection_and_error_analysis.md` (formal model selection rationale balancing F1, robustness, calibration, and CPU speed; failure taxonomy; practical limitations).

**GitHub Expectations:** Commit `eval(step-015): add Grad-CAM, FFT explainability, failure analysis, and model selection` → push to `main`.

**Verification Checklist:**
- [ ] Correct predictions AND failure cases (both FP and FN) visualized with Grad-CAM.
- [ ] Clear written justification explains *why* the final model was selected over the other 3 models.
- [ ] **GATE 4 PASS:** All Part 3–5 experiments, tables, and figures frozen; `PROGRESS_TRACKER.md` updated.

---

# PART 6 — INDUSTRY-ORIENTED WORKING COMPUTER VISION APPLICATION

> Satisfies Assignment Section **3F**: a functional Computer Vision app (Streamlit) accepting image/camera input, producing meaningful predictions + visualizations, and gracefully handling unsupported/invalid inputs.

---

## STEP-016 — Export Final Model Weights, Face-Crop Inference Engine & Input Validator  **[L][M5]**

**Title:** Package the selected model into a clean, CPU-friendly Python inference module with automatic face detection/cropping.

**Objective:** Download the winning model checkpoint from Kaggle, build a standalone inference module (`07_app/inference.py`) that:
1. Validates input files (extension, magic bytes, file size, image decode safety, minimum dimensions),
2. Runs **automatic Face Detection & Cropping** (OpenCV DNN face detector / MediaPipe with clean margin) so uncropped real-world photos and webcam frames match the cropped-face distribution of `DS0001`,
3. Computes prediction (`Real` vs. `AI-Generated`), calibrated probability, e-KYC risk tier (`Low Risk / Manual Review / High Risk`), **Grad-CAM heatmap overlay**, **2D FFT magnitude spectrum**, and inference latency (ms).

**Rubric Mapping:** Section 3F (practical workflow, invalid input handling), live-demo reliability.

**Prerequisites:** `STEP-015` complete (winning model & threshold locked).
**Estimated Time:** 2–3 hours.
**Parallelizable:** Can start scaffolding while `STEP-015` finishes.

**Inputs:** Winning model checkpoint (hosted in Kaggle/GitHub Release; config & threshold in `07_app/model_config.json`).

**Expected Outputs:**
- `07_app/model_config.json` (model architecture name, img_size, calibrated threshold, risk tier cutoffs, normalization constants, checkpoint download URL / local path)
- `07_app/validator.py` (handles non-image files, corrupt bytes, zero-byte files, oversized files, grayscale/RGBA conversion)
- `07_app/face_detector.py` (detects & crops primary face with configurable margin; returns clear warning if 0 faces or multiple faces detected, with optional override)
- `07_app/inference.py` (loads model, runs prediction + Grad-CAM + FFT spectrum + latency timer).

**GitHub Expectations:** Commit `feat(step-016): build inference engine, face cropper, and input validator` → push to `main` *(do not commit large `.pth` weights directly — document download link or use GitHub Release)*.

**Verification Checklist:**
- [ ] Inference runs smoothly on CPU (`< 500 ms` per image including Grad-CAM).
- [ ] Gracefully rejects `.txt`/`.pdf`/corrupted `.jpg` without crashing.
- [ ] Correctly detects and crops faces on uncropped full-body/portrait photos.

---

## STEP-017 — Build Streamlit Industry e-KYC Vision Application  **[L][M5]**

**Title:** Develop the interactive Streamlit web application for e-KYC Synthetic Face Verification.

**Objective:** Create a polished, industry-styled **Streamlit** application (`07_app/app.py`) demonstrating the full practical e-KYC verification workflow:
- **3 Input Modes:** (1) Image Upload (JPG/PNG/WEBP), (2) Live Webcam Capture (`st.camera_input`), (3) Built-in Sample Gallery (Real + AI-Generated test examples for fail-safe classroom demo).
- **Visual Outputs:** Original image with face bounding box, cropped face input, **Verdict Banner** (`Authentic Human Face` vs. `Suspected AI-Generated Face`), Confidence Gauge & e-KYC Risk Decision (`Approve / Manual Review / Reject`), **Grad-CAM Heatmap Overlay**, **2D FFT Spectrum**, and Latency/Model Metadata panel.
- **Error & Edge-Case UX:** Clear user-friendly banners for unsupported file types, corrupted images, no-face images (e.g., car/landscape photo), and low-resolution warnings.

**Rubric Mapping:** Section 3F (functional Streamlit app, image/camera input, annotated/visualized output, invalid input handling), Report Section 13, Presentation Topic 8.

**Prerequisites:** `STEP-016` complete.
**Estimated Time:** 3 hours.
**Parallelizable:** No.

**Inputs:** `07_app/inference.py`, `07_app/face_detector.py`, `07_app/validator.py`, 4–6 small demo sample images (`07_app/demo_samples/`).

**Expected Outputs:**
- `07_app/app.py` (clean, modular Streamlit UI)
- `07_app/README.md` (exact 3-line launch instructions: `streamlit run 07_app/app.py`)
- `07_app/demo_samples/` (2 Real + 2 AI-Generated + 1 non-face invalid test image for live demo backup).

**GitHub Expectations:** Commit `feat(step-017): implement Streamlit e-KYC vision application` → push to `main`.

**Verification Checklist:**
- [ ] `streamlit run 07_app/app.py` starts cleanly with zero console errors.
- [ ] Upload, webcam, and sample-gallery modes all produce full prediction + Grad-CAM + FFT outputs.
- [ ] Uploading a landscape/non-face image or corrupt file displays a clean handled warning (no traceback!).

---

## STEP-018 — End-to-End App Testing, Screenshot Capture & Live Demo Rehearsal  **[L][M5][All]**

**Title:** Run formal test cases on the vision app, capture report screenshots, and rehearse the live presentation demo.

**Objective:** Execute an 8-case test suite (valid real face, valid AI face, uncropped portrait, webcam photo, blurry/compressed face, non-face image, unsupported `.txt`/`.pdf` file, corrupted image), record pass/fail evidence, and capture crisp UI screenshots for Report Section 13 and the Presentation.

**Rubric Mapping:** Section 3F (practical workflow + invalid input handling), Report Section 13 (application screenshots required), Presentation Topic 8 (1.50 Marks).

**Prerequisites:** `STEP-017` complete.
**Estimated Time:** 1–2 hours.
**Parallelizable:** No.

**Inputs:** Running Streamlit app (`07_app/app.py`).

**Expected Outputs:**
- `07_app/test_app_pipeline.py` (automated pytest suite covering validator + face detector + inference)
- `07_app/uat_test_results.md` (8-scenario test table: Test ID, Input Type, Expected Behavior, Observed Result, Status)
- Screenshots in `06_evaluation/figures/app/`:
  - `fig16_app_real_prediction.png`
  - `fig17_app_fake_prediction_gradcam.png`
  - `fig18_app_invalid_input_handling.png`

**GitHub Expectations:** Commit `test(step-018): verify Streamlit app with automated tests and UAT screenshots` → push to `main`.

**Verification Checklist:**
- [ ] Automated pytest suite passes 100%.
- [ ] All 3 app screenshots saved, crisp, and registered in `06_evaluation/figure_registry.csv`.
- [ ] **GATE 5 PASS:** Working app tested end-to-end; backup local demo verified offline.

---

# PART 7 — FINAL PROJECT REPORT (PDF), PRESENTATION & SUBMISSION AUDIT

> Satisfies Assignment Sections **4, 5, 6 (17 mandatory report sections), 7 (10 presentation topics + mandatory 5-ID footers), and 8 (Final PDF Submission by Monday, 14 December 2026)**.

---

## STEP-019 — Compile 17-Section Final Project Report (PDF) & AI Usage Declaration  **[H][L][All]**

**Title:** Write, assemble, and export the complete 17-section PDF project report.

**Objective:** Author and verify the complete technical report containing **every single one of the 17 mandatory sections** from Assignment Section 6, embedding all real tables (`table01`–`table05`), high-res figures (`fig01`–`fig18`), team contribution table, and honest **AI Usage Declaration (< 25%)**, then export to clean PDF.

**Rubric Mapping:** Assignment Section 6 (all 17 sections), Section 4, Section 5, Section 8 (PDF deliverable).

**Prerequisites:** `STEP-018` complete (all results, figures, and app screenshots frozen).
**Estimated Time:** 4–6 hours (divided across all 5 members).
**Parallelizable:** Yes — each member drafts their sections simultaneously!

**Mandatory 17-Section Ownership Map:**

| Report Section | Author | Source Evidence in Repo |
|---|---|---|
| 1. **Cover Page** (Title, course, group #, all 5 full names & full student IDs) | M1 | `01_management/team_charter.md` |
| 2. **Abstract** | M1 + All | Final `table04_final_model_comparison.csv` |
| 3. **Industry Background & CV Problem Statement** | M1 | `01_management/team_charter.md` |
| 4. **Related Work** (≥3 real peer-reviewed references, e.g., Rahman et al. 2023 ArtiFact, Wang et al. 2020 CNNDetection, Ojha et al. 2023 UniversalFakeDetect, Selvaraju et al. 2017 Grad-CAM) | M1 + M3 | Verified citations only |
| 5. **Proposed Vision Solution & System Architecture** | M3 + M5 | End-to-end architecture diagram (`fig00_system_architecture.png`) |
| 6. **Image Dataset, Annotation Format & Data Splits** (+ rights & privacy/safety) | M1 | `02_data/dataset_card.md`, `split_verification_report.md` |
| 7. **Visual Dataset Exploration & Sample Images** | M2 | `fig01`–`fig05`, `eda_report.md` |
| 8. **Image Preprocessing & Augmentation** | M2 | `03_preprocessing/transforms.py`, `fig06` |
| 9. **Vision Models, Baselines & Experimental Setup** | M3 | `table01`, `fig07`, `fig08`, `experiment_registry.csv` |
| 10. **Optimization, Fine-Tuning & Ablation Results** | M4 | `table02`, `table03`, `fig09`, `fig10` |
| 11. **Task-Specific Evaluation & Model Comparison** | M4 | `table04`, `table05`, `fig11`, `fig12` |
| 12. **Prediction Visualizations, Explainability & Error Analysis** | M4 | `fig13`–`fig15`, `model_selection_and_error_analysis.md` |
| 13. **Working Computer Vision Application & Industry Relevance** | M5 | `fig16`–`fig18`, `uat_test_results.md` |
| 14. **Discussion, Limitations & Future Work** | All | Unseen generators, face-crop dependency, fairness/demographic bias |
| 15. **Individual Team Member Contributions** (Full IDs + actual % = 100%) | All | `01_management/team_contributions.csv` |
| 16. **AI Usage Declaration** (Tools, purposes, affected sections, estimated % `< 25%`) | All | `01_management/ai_usage_log.md` |
| 17. **References** (Formatted IEEE/APA — zero fabricated references!) | M1 | Verified DOIs / arXiv / conference venues |

**Expected Outputs:**
- `08_report/report_source.md` (or `.tex` / `.docx` source)
- `08_report/Final_CV_Project_Report.pdf` (final submission-ready PDF)

**GitHub Expectations:** Commit `docs(step-019): compile 17-section final project report PDF` → push to `main`.

**Verification Checklist:**
- [ ] All 17 sections present in exact order with clear numbering.
- [ ] All 5 members' **full names and full student IDs** on Cover Page and Section 15.
- [ ] Every table/figure number matches `06_evaluation/` with zero discrepancies.
- [ ] Dataset usage rights (MIT) and privacy/safety considerations explicitly discussed.
- [ ] AI Usage Declaration included and strictly `< 25%`.
- [ ] At least 3 genuine, verified academic references cited.

---

## STEP-020 — Presentation Deck (5-ID Footers), Live Demo Check & Final Submission Audit  **[H][All]**

**Title:** Build the in-class presentation slides, verify report–slide consistency, and submit the PDF by **Monday, 14 December 2026**.

**Objective:** Prepare crisp presentation slides covering all **10 mandatory presentation topics** (Assignment Section 7), enforce the **mandatory readable footer containing all 5 full student IDs on EVERY slide**, rehearse each member's speaking part + live Streamlit demo, and submit ONLY the PDF report on time.

**Rubric Mapping:** Assignment Section 7 (Presentation: **8 Marks** — largest grade component!) & Section 8 (Final Submission Requirements).

**Prerequisites:** `STEP-019` complete.
**Estimated Time:** 3–4 hours.
**Parallelizable:** Yes (each member prepares their own slides).

**Mandatory 10-Topic Slide Map (Suggested ~14–16 Slides):**
1. **Title Slide:** Project title, industry domain, all 5 full names & full student IDs (`M1`)
2. **Industry Problem, Objectives & Proposed Vision Solution** (`M1`)
3. **Dataset (`DS0001`), Annotations, License & Visual Sample Grid** (`M1` / `M2`)
4. **Visual EDA, Preprocessing, Training-Only Augmentation & Leak-Free Splits** (`M2`)
5. **Vision Architectures (4 Models, 3 Families), Baselines & Optimization Strategy** (`M3`)
6. **Quantitative Model Comparison, Optimization Before/After & Ablation Results** (`M3` / `M4`)
7. **Qualitative Outputs, Grad-CAM / FFT Explainability & Failure-Case Analysis** (`M4`)
8. **Live Working Computer Vision Application Demonstration** (`M5` — live Streamlit demo + backup screenshots)
9. **Industry Benefits, Limitations & Future Improvements** (`M5` / `M1`)
10. **Individual Contributions Table & AI Usage Declaration (<25%)** (`All`)

**Expected Outputs:**
- `09_presentation/slide_outline_and_script.md` (speaker assignments, timing per member, Q&A prep)
- Presentation slides file (PowerPoint / Google Slides / PDF — **brought to class; DO NOT submit per Section 8**)
- Final `PROGRESS_TRACKER.md` with all 20 steps marked `DONE`.

**GitHub Expectations:** Commit `docs(step-020): finalize presentation script and pass final submission audit` → push to `main`.

**Final Submission Audit Checklist (GATE 6 — MUST PASS 100%):**
- [ ] **PDF Report ONLY** submitted by **Monday, 14 December 2026** (do NOT submit presentation slides).
- [ ] All 5 students' full IDs appear on the **title slide AND in a readable footer on EVERY slide**.
- [ ] All numbers in slides are 100% identical to the submitted PDF report.
- [ ] Every single member has rehearsed explaining their own assigned work and Q&A.
- [ ] Working Streamlit app tested on the presentation laptop (with offline fallback sample images ready).
- [ ] Evidence links (GitHub repo + Kaggle notebooks) updated in course progress-tracking spreadsheet if applicable.
