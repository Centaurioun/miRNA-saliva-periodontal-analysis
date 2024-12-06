import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_pearson_correlation(df):
    correlation_matrix = df.corr(method='pearson')
    return correlation_matrix

def visualize_correlation_heatmap(correlation_matrix):
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Pearson Correlation Heatmap')
    plt.show()

def main():
    # Load data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_data(processed_data_path)

    # Calculate Pearson correlation
    correlation_matrix = calculate_pearson_correlation(df)
    print(correlation_matrix)

    # Visualize correlation heatmap
    visualize_correlation_heatmap(correlation_matrix)

if __name__ == "__main__":
    main()
