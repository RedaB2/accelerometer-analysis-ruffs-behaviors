# Accelerometer Analysis of Ruff Behaviors

## Authors
- Srujan Gowda Sathiganahally Jagadeesha — sathigan@usc.edu
- Reda Boutayeb — boutayeb@usc.edu
- Rohit Milind Sonawane — rsonawan@usc.edu

---

## Abstract
We build a pipeline for behavior classification from high-frequency tri-axial accelerometers, covering calibration and synchronization, windowing and feature extraction, modeling with HMMs, Random Forests, and neural networks, and rigorous evaluation. We target across-individual generalization via leave-one-bird-out validation, per-class F1, calibration curves, and rare-class error analysis. Success means improved macro-F1 and interpretable behavior-level insights.

---

## Problem
**Goal:** Predict 13 distinct behaviors from continuous accelerometry streams.  
**Motivation:** Quantify activity budgets for ecological insight, health monitoring, and conservation planning at scale.  
**Challenges:** Noisy time series and sensor drift, overlapping kinematics, long multi-day recordings, label scarcity and imbalance, and cross-individual generalization.

---

## Prior Work and Baselines
- **HMM-based pipelines:** Temporal structure and interpretability, sensitive to feature quality.
- **Random Forests on engineered features:** Strong tabular baseline.
- **Deep learning for HAR (LSTM, 1D-CNN, hybrids):** Captures nonlinear sequential patterns; requires careful regularization and data volume.
- **Probability calibration:** Improves decision thresholds and downstream interpretability.

---

## Dataset
- **Source:** Edmond archive (~81 GB). Includes raw tri-axial accelerometry for ~30 birds, deployment notes, behavior labels, calibration sessions.
- **Format:** SQLite database (e.g., `ruff-acc.db`) with synchronized timestamps and label tables.
- **Imbalance:** Rare behaviors require stratified sampling and cost-sensitive learning.

---

## Methods

### 1) Pre-processing
- Re-run calibration and time synchronization.
- Windowing: grid search 1–5 s with overlap.
- Feature extraction: time-domain stats, static/dynamic acceleration, jerk, signal magnitude area, FFT band energies, pitch/roll from orientation.

### 2) Models
- Baselines: HMM, Random Forest.
- Neural: LSTM, 1D-CNN, and CNN+GRU hybrids with dropout and weight decay.
- Class imbalance: focal loss or class weights; mixup and time-warp augmentations.
- Calibration: temperature scaling or isotonic regression.

### 3) Evaluation
- **Primary:** macro-F1 across 13 behaviors.
- **Secondary:** per-class F1/recall, AUROC, log-loss, calibration error (ECE), confusion matrices.
- **Generalization:** leave-one-bird-out cross-validation.
- **Ablations:** window size, feature sets, model depth, augmentation on/off.

### 4) Success Criteria
- Meet or exceed established repository baselines on macro-F1.
- Improve calibration while maintaining or improving accuracy.
- Provide interpretable behavior-level insights and error analyses.

---


## Results (planned)
- Report macro-F1 and per-class metrics for all models.
- Calibration curves and reliability diagrams.
- Error analysis for rare behaviors and confusion hotspots.

---

## Timeline
- **Week 1–2:** Data audit, calibration, and synchronization.
- **Week 3:** Windowing and feature engineering.
- **Week 4:** Baselines (HMM, RF) and initial metrics.
- **Week 5–6:** Neural models and augmentation.
- **Week 7:** Calibration and interpretability.
- **Week 8:** Final evaluation, report, and poster.

---
