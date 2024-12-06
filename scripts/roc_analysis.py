import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_roc_auc(df, target, predictor):
    fpr, tpr, _ = roc_curve(df[target], df[predictor])
    roc_auc = auc(fpr, tpr)
    return fpr, tpr, roc_auc

def calculate_precision_recall(df, target, predictor):
    precision, recall, _ = precision_recall_curve(df[target], df[predictor])
    return precision, recall

def plot_roc_curve(fpr, tpr, roc_auc, title='ROC Curve'):
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:0.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()

def plot_precision_recall(precision, recall, title='Precision-Recall Curve'):
    plt.figure()
    plt.plot(recall, precision, color='blue', lw=2)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title(title)
    plt.show()

def main():
    # Load data
    raw_data_path = '../data/raw/Kasim2024-son-veri.csv'
    processed_data_path = '../data/processed/cleaned_data.csv'
    
    raw_df = load_data(raw_data_path)
    processed_df = load_data(processed_data_path)

    # Define target and predictors
    target = 'ClinicalParam1'
    predictors = ['miRNA1', 'miRNA2', 'miRNA3', 'GAPDH']

    for predictor in predictors:
        # Calculate ROC AUC for raw data
        fpr, tpr, roc_auc = calculate_roc_auc(raw_df, target, predictor)
        print(f'ROC AUC for {predictor} (raw): {roc_auc}')
        plot_roc_curve(fpr, tpr, roc_auc, title=f'ROC Curve for {predictor} (raw)')

        # Calculate ROC AUC for processed data
        fpr, tpr, roc_auc = calculate_roc_auc(processed_df, target, predictor)
        print(f'ROC AUC for {predictor} (processed): {roc_auc}')
        plot_roc_curve(fpr, tpr, roc_auc, title=f'ROC Curve for {predictor} (processed)')

        # Calculate precision-recall for raw data
        precision, recall = calculate_precision_recall(raw_df, target, predictor)
        plot_precision_recall(precision, recall, title=f'Precision-Recall Curve for {predictor} (raw)')

        # Calculate precision-recall for processed data
        precision, recall = calculate_precision_recall(processed_df, target, predictor)
        plot_precision_recall(precision, recall, title=f'Precision-Recall Curve for {predictor} (processed)')

if __name__ == "__main__":
    main()
