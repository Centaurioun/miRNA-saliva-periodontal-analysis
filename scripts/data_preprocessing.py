import pandas as pd
from sklearn.preprocessing import RobustScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Handle missing data
    df = df.dropna()
    return df

def robust_scale_data(df, columns_to_scale):
    scaler = RobustScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    return df

def generate_descriptive_statistics(df):
    return df.describe()

def main():
    # Load data
    raw_data_path = '../data/raw/Kasim2024-son-veri.csv'
    df = load_data(raw_data_path)

    # Clean data
    df = clean_data(df)

    # Robust scaling normalization
    columns_to_scale = ['miRNA1', 'miRNA2', 'miRNA3', 'GAPDH']
    df = robust_scale_data(df, columns_to_scale)

    # Generate descriptive statistics
    stats = generate_descriptive_statistics(df)
    print(stats)

    # Save processed data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df.to_csv(processed_data_path, index=False)

if __name__ == "__main__":
    main()
