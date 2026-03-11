# 💳 Financial Fraud Detection & Anomaly Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange)
![Imbalanced-Learn](https://img.shields.io/badge/Imbalanced--Learn-SMOTE-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 📌 Project Overview
This project tackles one of the most difficult challenges in data science: severe class imbalance. Using a dataset of 250,000+ credit card transactions where only 0.2% are fraudulent, this project builds a robust classification pipeline designed to maximize fraud detection (Recall) rather than misleading baseline accuracy.

## 🛠️ Technical Architecture & Workflow
1. **Data Ingestion & EDA:** Analyzed anonymized PCA features (V1-V30) to understand distribution and the 99.8% / 0.2% class imbalance.
2. **Train/Test Splitting:** Isolated a 20% holdout test set *before* applying any balancing techniques to prevent data leakage and artificially inflated scores.
3. **Algorithmic Balancing (SMOTE):** Deployed the Synthetic Minority Over-sampling Technique (SMOTE) strictly on the training data to synthesize mathematically viable fraud cases, giving the model a balanced training environment.
4. **Ensemble Modeling:** Trained a `RandomForestClassifier` to capture complex, non-linear fraud patterns.
5. **Threshold Tuning for Business Value:** Identified that a standard 50% probability threshold yielded an unacceptable False Negative rate (missed fraud). Extracted raw `predict_proba` values and lowered the decision threshold to 15%, drastically increasing the Recall metric to align with real-world banking risk profiles.
6. **Feature Importance:** Extracted internal model weights to identify the top hidden features (V10, V5, V8) driving fraudulent transactions.

## 📊 The "Accuracy Paradox"
A model that predicts "Normal" 100% of the time on this dataset will achieve 99.8% Accuracy, while failing completely at its business objective. 

By analyzing the **Confusion Matrix** and tuning the probability thresholds, this model optimizes for **Recall**—minimizing the catastrophic multi-million dollar costs of False Negatives (missed fraud) in exchange for a manageable increase in False Positives (customer alerts).

## 👨‍💻 Author
**David**
