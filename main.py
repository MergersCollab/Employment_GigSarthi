import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


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


def plot_clusters(df):
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

    # Show graph
    plt.show()

# MAIN BLOCK
if __name__ == "__main__":
    
    # Load dataset
    df = pd.read_csv("data/raw/gig_dirty_data.csv")

    # Apply clustering
    df = worker_intelligence(df)

    # Print output
    print(df.head())

    # Plot clusters
    plot_clusters(df)