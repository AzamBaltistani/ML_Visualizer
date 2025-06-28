import pandas as pd
from sklearn.cluster import KMeans

def run_kmeans(points_df: pd.DataFrame, n_clusters: int):
    """
    Run KMeans on the input points dataframe with specified number of clusters.
    Returns the dataframe with cluster labels and the centroids.
    """
    model = KMeans(n_clusters=n_clusters, n_init='auto')
    cluster_labels = model.fit_predict(points_df[["X", "Y"]])
    centers = model.cluster_centers_

    points_df["cluster"] = cluster_labels
    return points_df, centers
