# computer-vission-course-work

**Industry-Oriented End-to-End Computer Vision Application Development (Fall 2026)**  
**Single Source of Truth:** `https://github.com/isthisdeception/computer-vission-course-work`

---

## Project Overview

| Field | Value |
|---|---|
| **Project Title** | AI-Generated Face Detection for Digital Identity Verification (e-KYC) and Fraud Prevention |
| **Industry Domain** | Cybersecurity / Finance & Banking (e-KYC & Trust/Safety) |
| **Primary Dataset (Single Dataset)** | `DS0001` — ArtiFact Face Subset (`kaggle:isthisdeception/ds0001-artifact-face-subset`) |
| **Dataset Summary** | 50,000 face images — 25,000 Real / 25,000 Fake across 13 AI generators (GANs, Diffusion, Transformers, Inpainting, 3D Synthetics), MIT License |
| **Team Size** | Exactly 5 Students |
| **Grading Weight** | Project Assignment: **5 Marks** + Presentation: **8 Marks** = **13 Marks** |
| **Final Report Deadline** | **Monday, 14 December 2026** (PDF Report Submission) |
| **AI Usage Policy** | Strictly **< 25%** of substantive work + mandatory AI Usage Declaration |

---

## Single Source of Truth & Workflow Rules

1. **GitHub = Single Source of Truth:** Every blueprint step, split CSV, experiment config, evaluation table, figure, app script, team log, and report artifact lives in this repository.
2. **Kaggle = Data & GPU Training Tier:** Raw images (`DS0001`) stay on Kaggle (`kaggle:isthisdeception/ds0001-artifact-face-subset`). Image bytes and heavy `.pth` weights are **never** pushed to GitHub.
3. **Sequential Execution:** Follow [`PROJECT_EXECUTION_BLUEPRINT.md`](./PROJECT_EXECUTION_BLUEPRINT.md) strictly from `STEP-001` to `STEP-020`. Track live status in [`PROGRESS_TRACKER.md`](./PROGRESS_TRACKER.md).
4. **Academic Integrity & AI Limit (< 25%):** All 5 team members must execute, verify, and understand their assigned work. Log any AI assistance in `01_management/ai_usage_log.md` to guarantee compliance with the `< 25%` cap.

---

## Key Documents

- [`PROJECT_EXECUTION_BLUEPRINT.md`](./PROJECT_EXECUTION_BLUEPRINT.md) — Complete A–Z 20-step execution manual (`STEP-001` to `STEP-020`), mapped to every rubric item.
- [`PROGRESS_TRACKER.md`](./PROGRESS_TRACKER.md) — Live status board for all 20 steps, owners, and commit hashes.

---

## Planned Repository Structure (Created in `STEP-002`)

| Folder | Purpose |
|---|---|
| `01_management/` | Team charter, member contributions table, decision log, AI usage log (<25%) |
| `02_data/` | Dataset card (`DS0001`), license file, metadata pointers, leak-free split CSVs, EDA reports |
| `03_preprocessing/` | Preprocessing & training-only augmentation scripts, configs, and verification plots |
| `04_notebooks/` | Reproducible Kaggle notebooks (`01_eda.ipynb` … `08_evaluation_xai.ipynb`) |
| `05_models/` | Model architectures, experiment configs, training logs, and model comparison registry |
| `06_evaluation/` | Quantitative metrics CSVs, confusion matrices, per-generator breakdowns, Grad-CAM & FFT figures, error analysis |
| `07_app/` | Working Streamlit Computer Vision application (face detector/cropper + inference + Grad-CAM + edge-case handling) |
| `08_report/` | 17-section Final Project Report source + final exported PDF |
| `09_presentation/` | Presentation slide outline, asset links, demo script (slides brought to class, not submitted) |

---

## Team Members & Core Responsibilities

| Role | Student Name | Full Student ID | Primary Responsibilities | Target Share |
|---|---|---|---|---|
| **Member 1** | *TBD (STEP-001)* | *TBD* | Industry problem, `DS0001` dataset & license review, leak-free splits | 20% |
| **Member 2** | *TBD (STEP-001)* | *TBD* | Visual EDA, preprocessing & training-only augmentation | 20% |
| **Member 3** | *TBD (STEP-001)* | *TBD* | 4 vision model architectures across 3 families & baseline experiments | 20% |
| **Member 4** | *TBD (STEP-001)* | *TBD* | 3 optimizations, ablation study, task-specific evaluation & XAI visualizations | 20% |
| **Member 5** | *TBD (STEP-001)* | *TBD* | Streamlit vision application, face-crop integration, testing & deployment | 20% |

---

## Quick Roadmap (25 Nov → 14 Dec 2026)

- **Part 1 (`STEP-001`–`STEP-002`):** Team charter, scope lock, repo skeleton & environment setup
- **Part 2 (`STEP-003`–`STEP-006`):** `DS0001` verification, visual EDA, leak-free splits (70/15/15), preprocessing & augmentation
- **Part 3 (`STEP-007`–`STEP-010`):** 4 models across 3 families (Traditional CV FFT+LBP+SVM/RF, ResNet-50, EfficientNet-B0, ViT-B/16)
- **Part 4 (`STEP-011`–`STEP-013`):** 3 optimizations (Optimizer/LR, Robustness Augmentation, Threshold/Fine-tuning) + Controlled Ablation
- **Part 5 (`STEP-014`–`STEP-015`):** Test-set evaluation, per-generator breakdown, latency benchmark, Grad-CAM, FFT & failure-case analysis
- **Part 6 (`STEP-016`–`STEP-018`):** Working Streamlit e-KYC vision app (face detection/crop + prediction + Grad-CAM + invalid input handling) & testing
- **Part 7 (`STEP-019`–`STEP-020`):** 17-section PDF report, AI declaration (<25%), presentation slides (with 5-ID footer on every slide) & final audit
