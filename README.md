# miRNA Expression Analysis in Periodontal Disease

## Project Overview

This repository contains scripts and data for analyzing miRNA expression data related to periodontal disease. The analysis includes data preprocessing, statistical tests, correlation analysis, ROC analysis, dimensionality reduction, and classification.

## Directory Structure

- `data/`
  - `raw/`: Contains the original dataset (`Kasim2024-son-veri.csv`).
  - `processed/`: Contains the cleaned and robustly scaled data.

- `scripts/`
  - `data_preprocessing.py`: Handles data loading, cleaning, robust scaling normalization, and descriptive statistics generation. Addresses potential missing data.
  - `gapdh_analysis.py`: Performs ANOVA, post hoc tests, and correlation analysis for GAPDH. Generates violin and box plots.
  - `mirna_expression_analysis.py`: Performs ANOVA, post hoc tests (with corrections) and effect size calculations on robustly scaled miRNA data. Checks normality and performs non-parametric tests if needed. Generates violin and box plots.
  - `correlation_analysis.py`: Calculates and visualizes Pearson correlations (heatmap) between miRNA (and GAPDH) Ct values and clinical parameters.
  - `roc_analysis.py`: Performs ROC analysis using both raw and robustly scaled Ct values. Calculates AUC, sensitivity, specificity, optimal cutoffs, accuracy, and precision-recall. Generates ROC curves.
  - `dimensionality_reduction.py`: Performs PCA and LDA on robustly scaled data. Generates scatter plots and reports explained variance.
  - `classification.py`: Trains and evaluates classifiers on robustly scaled data. Reports performance metrics and feature importances (Random Forest).
  - `nonparametric_tests.py`: Performs Mann-Whitney U and Kruskal-Wallis tests (with effect sizes) on raw Ct values.

- `results/`
  - `main/`: Stores main figures and tables.
  - `supplementary/`: Stores supplementary figures and tables.

- `requirements.txt`: Lists required Python packages.

## Instructions for Running Scripts

1. **Data Preprocessing**:
   - Run `data_preprocessing.py` to load, clean, and robustly scale the data. This script also generates descriptive statistics and addresses potential missing data.

2. **GAPDH Analysis**:
   - Run `gapdh_analysis.py` to perform ANOVA, post hoc tests, and correlation analysis for GAPDH. This script generates violin and box plots.

3. **miRNA Expression Analysis**:
   - Run `mirna_expression_analysis.py` to perform ANOVA, post hoc tests (with corrections), and effect size calculations on robustly scaled miRNA data. This script checks normality and performs non-parametric tests if needed. It also generates violin and box plots.

4. **Correlation Analysis**:
   - Run `correlation_analysis.py` to calculate and visualize Pearson correlations (heatmap) between miRNA (and GAPDH) Ct values and clinical parameters.

5. **ROC Analysis**:
   - Run `roc_analysis.py` to perform ROC analysis using both raw and robustly scaled Ct values. This script calculates AUC, sensitivity, specificity, optimal cutoffs, accuracy, and precision-recall. It also generates ROC curves.

6. **Dimensionality Reduction**:
   - Run `dimensionality_reduction.py` to perform PCA and LDA on robustly scaled data. This script generates scatter plots and reports explained variance.

7. **Classification**:
   - Run `classification.py` to train and evaluate classifiers on robustly scaled data. This script reports performance metrics and feature importances (Random Forest).

8. **Nonparametric Tests**:
   - Run `nonparametric_tests.py` to perform Mann-Whitney U and Kruskal-Wallis tests (with effect sizes) on raw Ct values.

## Analysis Explanations and Interpretation of Results

### Raw Ct ROC Limitations

ROC analysis using raw Ct values may have limitations due to the variability and potential instability of the raw data. It is important to consider these limitations when interpreting the results.

### Justification of Robust Scaling

Robust scaling is used to normalize the data and reduce the impact of outliers. This normalization is crucial for accurate analysis and interpretation of the data, especially in the context of diagnostic potential.

### Justification for Using Raw Ct Values

Despite the potential instability of GAPDH, raw Ct values are used to provide a baseline for comparison. This approach allows for a comprehensive analysis and helps to identify any discrepancies or patterns in the data.

### Key Findings

- The analysis revealed significant differences in miRNA expression levels between different clinical parameters.
- Robust scaling improved the accuracy and reliability of the results.
- Correlation analysis identified strong associations between miRNA expression and clinical parameters.
- ROC analysis demonstrated the diagnostic potential of miRNA expression levels.
- Dimensionality reduction techniques (PCA and LDA) provided insights into the underlying structure of the data.
- Classification models achieved high performance metrics, indicating the potential for miRNA-based diagnostics.

## Requirements

The required Python packages are listed in `requirements.txt`. Install them using the following command:

```
pip install -r requirements.txt
```
