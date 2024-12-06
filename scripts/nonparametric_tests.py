import pandas as pd
import scipy.stats as stats
from pingouin import compute_effsize

def load_data(file_path):
    return pd.read_csv(file_path)

def perform_mann_whitney_u_test(df, group_col, value_col):
    groups = df[group_col].unique()
    group1 = df[df[group_col] == groups[0]][value_col]
    group2 = df[df[group_col] == groups[1]][value_col]
    u_stat, p_value = stats.mannwhitneyu(group1, group2)
    effect_size = compute_effsize(df, dv=value_col, between=group_col, eftype='cohen')
    return u_stat, p_value, effect_size

def perform_kruskal_wallis_test(df, group_col, value_col):
    groups = df[group_col].unique()
    data = [df[df[group_col] == group][value_col] for group in groups]
    h_stat, p_value = stats.kruskal(*data)
    effect_size = compute_effsize(df, dv=value_col, between=group_col, eftype='cohen')
    return h_stat, p_value, effect_size

def main():
    # Load data
    raw_data_path = '../data/raw/Kasim2024-son-veri.csv'
    df = load_data(raw_data_path)

    # Perform Mann-Whitney U test
    u_stat, p_value, effect_size = perform_mann_whitney_u_test(df, 'ClinicalParam1', 'GAPDH')
    print(f'Mann-Whitney U test results: U={u_stat}, p={p_value}, effect size={effect_size}')

    # Perform Kruskal-Wallis test
    h_stat, p_value, effect_size = perform_kruskal_wallis_test(df, 'ClinicalParam1', 'GAPDH')
    print(f'Kruskal-Wallis test results: H={h_stat}, p={p_value}, effect size={effect_size}')

if __name__ == "__main__":
    main()
