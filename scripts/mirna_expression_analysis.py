import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from pingouin import compute_effsize

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_anova(df, miRNA):
    model = ols(f'{miRNA} ~ C(ClinicalParam1)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    return anova_table

def perform_post_hoc_tests(df, miRNA):
    post_hoc_results = pairwise_tukeyhsd(df[miRNA], df['ClinicalParam1'])
    return post_hoc_results

def calculate_effect_size(df, miRNA):
    effect_size = compute_effsize(df, dv=miRNA, between='ClinicalParam1', eftype='cohen')
    return effect_size

def check_normality(df, miRNA):
    stat, p = stats.shapiro(df[miRNA])
    return p > 0.05

def perform_non_parametric_tests(df, miRNA):
    kruskal_result = stats.kruskal(df[miRNA], df['ClinicalParam1'])
    return kruskal_result

def generate_violin_plot(df, miRNA):
    sns.violinplot(x='ClinicalParam1', y=miRNA, data=df)
    plt.title(f'Violin plot of {miRNA} by ClinicalParam1')
    plt.show()

def generate_box_plot(df, miRNA):
    sns.boxplot(x='ClinicalParam1', y=miRNA, data=df)
    plt.title(f'Box plot of {miRNA} by ClinicalParam1')
    plt.show()

def main():
    # Load data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_data(processed_data_path)

    miRNAs = ['miRNA1', 'miRNA2', 'miRNA3']

    for miRNA in miRNAs:
        # Perform ANOVA
        anova_results = perform_anova(df, miRNA)
        print(f'ANOVA results for {miRNA}:')
        print(anova_results)

        # Perform post hoc tests
        post_hoc_results = perform_post_hoc_tests(df, miRNA)
        print(f'Post hoc results for {miRNA}:')
        print(post_hoc_results)

        # Calculate effect size
        effect_size = calculate_effect_size(df, miRNA)
        print(f'Effect size for {miRNA}:')
        print(effect_size)

        # Check normality
        is_normal = check_normality(df, miRNA)
        print(f'Normality test for {miRNA}: {"Normal" if is_normal else "Not normal"}')

        if not is_normal:
            # Perform non-parametric tests
            non_parametric_results = perform_non_parametric_tests(df, miRNA)
            print(f'Non-parametric test results for {miRNA}:')
            print(non_parametric_results)

        # Generate violin plot
        generate_violin_plot(df, miRNA)

        # Generate box plot
        generate_box_plot(df, miRNA)

if __name__ == "__main__":
    main()
