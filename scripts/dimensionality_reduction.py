import pandas as pd
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_pca(df, n_components=2):
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(df)
    explained_variance = pca.explained_variance_ratio_
    return principal_components, explained_variance

def perform_lda(df, target, n_components=2):
    lda = LDA(n_components=n_components)
    lda_components = lda.fit_transform(df.drop(columns=[target]), df[target])
    explained_variance = lda.explained_variance_ratio_
    return lda_components, explained_variance

def plot_scatter(data, labels, title, xlabel='Component 1', ylabel='Component 2'):
    plt.figure()
    for label in set(labels):
        plt.scatter(data[labels == label, 0], data[labels == label, 1], label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def main():
    # Load data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_data(processed_data_path)

    # Perform PCA
    pca_components, pca_explained_variance = perform_pca(df.drop(columns=['SampleID', 'ClinicalParam1', 'ClinicalParam2']))
    print(f'PCA explained variance: {pca_explained_variance}')
    plot_scatter(pca_components, df['ClinicalParam1'], title='PCA Scatter Plot')

    # Perform LDA
    lda_components, lda_explained_variance = perform_lda(df, target='ClinicalParam1')
    print(f'LDA explained variance: {lda_explained_variance}')
    plot_scatter(lda_components, df['ClinicalParam1'], title='LDA Scatter Plot')

if __name__ == "__main__":
    main()
