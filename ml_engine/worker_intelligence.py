import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def worker_intelligence(df):
    # Safety cleaning
    df = df.dropna()

    features = [
        'monthly_income',
        'repayment_history_pct',
        'employment_length',
        'utility_bill_average'
    ]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # KMeans Model
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    return df


def plot_clusters(df):
    sns.scatterplot(
        data=df,
        x='monthly_income',
        y='repayment_history_pct',
        hue='cluster',
        palette='viridis'
    )
    plt.title("Worker Segmentation using K-Means")
    plt.show()


# Example run (for testing)
if __name__ == "__main__":
    df = pd.read_csv("your_cleaned_dataset.csv")  # change path
    df = worker_intelligence(df)
    print(df.head())
    plot_clusters(df)