# Team Charter, Industry Problem Definition & Scope Lock (`STEP-001`)

> **Course:** Computer Vision Project-Based Assignment & Presentation (Fall 2026)  
> **Group:** `GROUP 08` (Team Size: Exactly 5 Students)  
> **Single Source of Truth:** `https://github.com/isthisdeception/computer-vission-course-work`  
> **Final Report Deadline:** Monday, 14 December 2026  
> **Date Locked:** 2026-11-25  

---

## 1. Project Identity & Team Roster (`GROUP 08`)

- **Project Title:** AI-Generated Face Detection for Digital Identity Verification (e-KYC) and Fraud Prevention
- **Industry Domain:** **Cybersecurity** *(applied to Finance & Banking digital onboarding / e-KYC fraud defense)*
- **Vision Task:** Binary Image Classification (`Real Human Face` vs. `AI-Generated Synthetic Face`) with Explainable Localization (Grad-CAM & 2D FFT) and Automated Face Detection/Cropping.

| Member | Student Full Name | Full Student ID | Assigned Responsibilities (Section 4) | Planned Share |
|---|---|---|---|---:|
| **Member 1** | Md Assaduzzaman | `0242310005101233` | Industry problem, `DS0001` dataset & license review, leak-free splits | 20% |
| **Member 2** | Khadijatul Kobra Keya | `0242310005101223` | Visual EDA, image preprocessing & training-only augmentation | 20% |
| **Member 3** | Mymuna Ibnat Priota | `0242310005101804` | 4 vision model architectures across 3 families & baseline experiments | 20% |
| **Member 4** | Odito Al Nafiu | `0242310005101253` | 3 optimizations, ablation study, task-specific evaluation & XAI visualizations | 20% |
| **Member 5** | Ishrat Jahan | `0242310005101164` | Working Streamlit vision application, face-crop integration & testing | 20% |
| **Total** | **5 Students** | — | **End-to-End Computer Vision Pipeline** | **100%** |

---

## 2. Industry Problem & Significance (Assignment Section 2)

### 2.1 The Industry Problem
Modern digital onboarding workflows in banking, fintech, telecom, and online marketplaces rely on **electronic Know Your Customer (e-KYC)** verification, where users submit selfie photos or ID portraits to open accounts and verify identity. Rapid advances in generative AI — including GANs (StyleGAN1/2/3, StarGAN, ProjectedGAN), Diffusion models (Stable Diffusion), Transformers (Taming Transformer), and neural inpainting/3D face synthesis — now enable fraudsters to manufacture photorealistic, non-existent human faces at near-zero cost.

Synthetic identities created with AI-generated faces bypass human visual inspection, enabling:
- Fraudulent bank/fintech account creation and money-mule networks,
- Synthetic identity loan defaults and payment chargebacks,
- Impersonation, phishing, and fake-account spam on digital platforms.

### 2.2 Significance
Human reviewers perform near chance level when distinguishing modern synthetic faces from real camera portraits. Traditional cybersecurity defenses (IP checks, metadata checks) fail because EXIF metadata is stripped during upload and social-media/browser compression obscures naive pixel artifacts. An automated, calibrated, and explainable **Computer Vision screening layer** is therefore critical to flag suspicious synthetic faces in real time before fraudulent accounts are approved.

---

## 3. Intended Users & Stakeholders

| Stakeholder Group | Practical Role & Need |
|---|---|
| **e-KYC / Fraud Analysts (Primary Users)** | Need fast automated screening (`Approve / Manual Review / Reject`) with visual evidence (Grad-CAM & frequency heatmaps) rather than an opaque black-box score. |
| **Banks, Fintechs & Telecom Onboarding Teams** | Need low-latency, low-false-positive verification that catches synthetic faces without blocking legitimate customers. |
| **Cybersecurity & Trust-and-Safety Engineers** | Need modular inference pipelines with strict input validation, degradation robustness (JPEG compression/blur), and measurable latency budgets. |
| **Compliance & Risk Auditors** | Require reproducible evaluation metrics, transparent failure-case documentation, and ethical/privacy-compliant dataset usage. |

---

## 4. Proposed Computer Vision-Based Solution

We design and implement an **end-to-end, industry-oriented AI-Generated Face Verification System**:

1. **Single Curated Multi-Generator Dataset (`DS0001`):**
   - **ArtiFact Face Subset** (`kaggle:isthisdeception/ds0001-artifact-face-subset`, Rahman et al., 2023; **MIT License**).
   - **50,000 face images** — strictly balanced (**25,000 Real / 25,000 Fake**) spanning **13 distinct synthetic generator families** (`stylegan1`, `stylegan2`, `stylegan3`, `stargan`, `projected_gan`, `gansformer`, `cips`, `sfhq`, `face_synthetics`, `stable_diffusion`, `taming_transformer`, `lama`, `mat`).
   - **Zero-leakage Stratified Split:** 70% Train (35,000) / 15% Validation (7,500) / 15% Test (7,500), stratified jointly by class and generator with MD5 hash-deduplication guards.
2. **Multi-Family Vision Modeling (4 Models across 3 Distinct Families):**
   - `M1` (**Traditional CV Baseline — Family 1):** Handcrafted 2D FFT radial spectrum + LBP texture + YCbCr color statistics → Random Forest / SVM.
   - `M2` (**Classic CNN — Family 2):** ImageNet-pretrained **ResNet-50** (explicitly comparing `M2a` frozen linear probe baseline vs. `M2b` full fine-tuning).
   - `M3` (**Lightweight Industry CNN — Family 2):** **EfficientNet-B0** (fine-tuned for high throughput and low CPU latency).
   - `M4` (**Vision Transformer — Family 3):** **ViT-B/16** (or Swin-Tiny) comparing global self-attention against local CNN inductive biases.
3. **Optimization & Controlled Ablation (3 Strategies + Ablation):**
   - `OPT-1`: Optimizer & LR scheduling (`Adam` constant LR vs. `AdamW` + Warmup + `CosineAnnealingLR` + label smoothing).
   - `OPT-2`: Robustness-aware training-only augmentation (JPEG compression, Gaussian blur, color jitter) verified on both clean and degraded test sets.
   - `OPT-3`: Validation-calibrated decision threshold tuning for e-KYC risk control (`FPR`-constrained operating point).
   - `ABL-1`: Controlled ablation quantifying robustness gain under compression/blur and/or unseen-generator hold-out generalization (`stable_diffusion` + `stylegan3` held out).
4. **Explainability & Diagnostics:**
   - **Grad-CAM** overlays highlighting facial artifact hotspots (eyes, skin micro-texture, hairline, background boundaries).
   - **2D FFT Log-Magnitude Spectrum** visualization comparing spectral signatures.
   - Per-generator detection breakdown across all 13 generators and structured False Positive / False Negative failure-case analysis.
5. **Working Industry Application (Streamlit):**
   - Accepts **image upload, webcam capture, or built-in sample images**.
   - Performs **input validation** (file format, corruption check, non-face rejection) and **automatic Face Detection & Cropping** so uncropped real-world portraits match the training domain.
   - Outputs verdict (`Authentic Human Face` vs. `Suspected AI-Generated Face`), calibrated confidence, **3-tier e-KYC Risk Decision** (`Low Risk — Approve`, `Medium Risk — Manual Review`, `High Risk — Flag/Reject`), Grad-CAM overlay, FFT plot, and inference latency (ms).

---

## 5. Expected Industry Benefits & Measurable Outcomes

| KPI / Outcome | Target Benchmark | Business Value |
|---|---|---|
| **Classification Performance (Test F1 / ROC-AUC)** | F1 ≥ 92%, ROC-AUC ≥ 0.96 on canonical 7.5k Test set | High accuracy across 13 diverse synthetic generators |
| **Compression Robustness (Degraded Test F1)** | Significant F1 retention gain vs. unaugmented baseline under JPEG q=60 + blur | Reliable screening on real web/mobile compressed uploads |
| **e-KYC False Positive Control** | Calibrated low-FPR operating point + Manual Review grey zone | Minimizes friction for legitimate human customers |
| **CPU Inference Speed** | < 500 ms/image end-to-end (including face crop + Grad-CAM) on standard CPU | Deployable without expensive GPU inference servers |
| **Analyst Trust & Auditability** | Visual Grad-CAM + FFT evidence per prediction + 100% handled invalid inputs | Actionable explanations for compliance & manual review queues |

---

## 6. Practical Application Workflow

```text
[User Upload / Webcam Portrait]
        │
        ▼
[1. Input Validator] ──(invalid format / corrupt / unreadable)──► [Clean Error Banner]
        │ (valid image)
        ▼
[2. Automatic Face Detector & Cropper] ──(no face detected)──► [Warning: No Face Found]
        │ (cropped aligned face, 224x224)
        ▼
[3. Winning Fine-Tuned Vision Model + Calibrated Threshold]
        │
        ├──► Verdict + Calibrated Probability + e-KYC Risk Tier (Approve / Review / Reject)
        ├──► Grad-CAM Artifact Heatmap Overlay + 2D FFT Spectrum
        └──► Inference Latency (ms) & Model Metadata
```

---

## 7. Governance, Scope Boundaries & Compliance Rules

- **Single Dataset Lock:** Only `DS0001` (`kaggle:isthisdeception/ds0001-artifact-face-subset`) is used for training, validation, testing, and ablation to guarantee depth and on-time completion by **Monday, 14 December 2026**.
- **Storage Tier Policy:** Raw image files and heavy model checkpoints (`.pth`/`.pt`) remain on Kaggle / local runtime and are never committed to GitHub. GitHub holds code, split CSVs, registries, evaluation tables, figures, app source, and report artifacts.
- **Academic Integrity & AI Usage Cap (`< 25%`):** Every team member independently performs, validates, and understands their assigned component. All AI assistance is transparently logged in `01_management/ai_usage_log.md` and strictly kept below `25%` of substantive work.
- **Milestone Synchronization:** Progress is updated after every milestone on both GitHub (`PROGRESS_TRACKER.md`) and the official course Google Sheet.
