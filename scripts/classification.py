import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def train_random_forest(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

def evaluate_classifier(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    return accuracy, report, conf_matrix

def plot_feature_importances(clf, feature_names):
    importances = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(len(importances)), importances[indices], align="center")
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.xlim([-1, len(importances)])
    plt.show()

def main():
    # Load data
    processed_data_path = '../data/processed/cleaned_data.csv'
    df = load_data(processed_data_path)

    # Prepare data for classification
    X = df.drop(columns=['SampleID', 'ClinicalParam1', 'ClinicalParam2'])
    y = df['ClinicalParam1']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train Random Forest classifier
    clf = train_random_forest(X_train, y_train)

    # Evaluate classifier
    accuracy, report, conf_matrix = evaluate_classifier(clf, X_test, y_test)
    print(f'Accuracy: {accuracy}')
    print('Classification Report:')
    print(report)
    print('Confusion Matrix:')
    print(conf_matrix)

    # Plot feature importances
    plot_feature_importances(clf, X.columns)

if __name__ == "__main__":
    main()
