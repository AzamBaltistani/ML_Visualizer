import pandas as pd
from sklearn.cluster import DBSCAN

def run_dbscan(points_df: pd.DataFrame, eps: float, min_samples: int):
    """
    Run DBSCAN on input points dataframe.
    
    Returns:
        - points_df with added 'cluster' column
        - number of clusters found
    """
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(points_df[["X", "Y"]])

    points_df["cluster"] = labels
    return points_df, len(set(labels)) - (1 if -1 in labels else 0)
