import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# =========================
# WORKER INTELLIGENCE
# =========================
def worker_intelligence(df):
    features = [
        'earnings_per_day',
        'hours_worked',
        'jobs_completed',
        'rating'
    ]

    # Convert to numeric (handles 'ten', etc.)
    for col in features:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove missing values
    df = df.dropna()

    # Remove invalid (negative values)
    df = df[
        (df['hours_worked'] >= 0) &
        (df['jobs_completed'] >= 0) &
        (df['earnings_per_day'] >= 0)
    ]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)

    return df


# =========================
# SCATTER PLOT (Segmentation)
# =========================
def plot_clusters(df):
    plt.figure()

    sns.scatterplot(
        data=df,
        x='earnings_per_day',
        y='jobs_completed',
        hue='cluster',
        palette='viridis'
    )

    plt.title("Worker Segmentation using K-Means")

    # Save image
    plt.savefig("cluster_plot.png")

    plt.show()


# =========================
# DISTRIBUTION PLOT (NEW)
# =========================
def plot_cluster_distribution(df):
    plt.figure()

    df['cluster'].value_counts().sort_index().plot(kind='bar')

    plt.title("Cluster Distribution Grpah: ")
    plt.xlabel("Cluster")
    plt.ylabel("Number of Workers")

    # Save image
    plt.savefig("cluster_distribution.png")

    plt.show()


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    # Load dataset
    df = pd.read_csv("data/raw/gig_dirty_data.csv")

    # Apply cleaning + clustering
    df = worker_intelligence(df)

    # Save cleaned + clustered data
    df.to_csv("cleaned_clustered_data.csv", index=False)

    # Show sample output
    print(df.head())

    # Generate graphs
    plot_clusters(df)
    plot_cluster_distribution(df)