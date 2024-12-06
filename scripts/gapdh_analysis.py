import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_anova(df):
    model = ols('GAPDH ~ C(ClinicalParam1)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table

def perform_post_hoc_tests(df):
    post_hoc_results = pairwise_tukeyhsd(df['GAPDH'], df['ClinicalParam1'])
    return post_hoc_results

def perform_correlation_analysis(df):
    correlation_matrix = df.corr()
    return correlation_matrix

def generate_violin_plot(df):
    sns.violinplot(x='ClinicalParam1', y='GAPDH', data=df)
    plt.title('Violin plot of GAPDH by ClinicalParam1')
    plt.show()

def generate_box_plot(df):
    sns.boxplot(x='ClinicalParam1', y='GAPDH', data=df)
    plt.title('Box plot of GAPDH by ClinicalParam1')
    plt.show()

def main():
    # Load data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_data(processed_data_path)

    # Perform ANOVA
    anova_results = perform_anova(df)
    print(anova_results)

    # Perform post hoc tests
    post_hoc_results = perform_post_hoc_tests(df)
    print(post_hoc_results)

    # Perform correlation analysis
    correlation_matrix = perform_correlation_analysis(df)
    print(correlation_matrix)

    # Generate violin plot
    generate_violin_plot(df)

    # Generate box plot
    generate_box_plot(df)

if __name__ == "__main__":
    main()
