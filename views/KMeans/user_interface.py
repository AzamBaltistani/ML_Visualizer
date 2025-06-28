import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from streamlit_drawable_canvas import st_canvas
from views.KMeans import kmean_algorithm

st.set_page_config(page_title="K-Means Visualizer", layout="wide")
st.title("K-Means Clustering Visualizer")

GRID_SIZE = 100
PIXELS = 400
CELL_SIZE = PIXELS // GRID_SIZE

if "kmeans_points" not in st.session_state:
    st.session_state.kmeans_points = []

col1, col2, col3 = st.columns([4, 4, 2], gap="small")

with col1:
    st.subheader("Input & Controls")

    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 255, 0.6)",
        stroke_width=0,
        width=PIXELS,
        height=PIXELS,
        drawing_mode="point",
        update_streamlit=True,
        key="kmeans_canvas",
    )

    if canvas_result.json_data and "objects" in canvas_result.json_data:
        new_points = []
        for obj in canvas_result.json_data["objects"]:
            x = int(obj["left"] // CELL_SIZE)
            y = GRID_SIZE - 1 - int(obj["top"] // CELL_SIZE)
            new_points.append((x, y))
        st.session_state.kmeans_points = new_points

    k = st.slider("Number of Clusters (k)", 1, 10, 3)

with col2:
    st.subheader("K-Means Clustering")

    points_df = pd.DataFrame(st.session_state.kmeans_points, columns=["X", "Y"])

    if not points_df.empty and len(points_df) >= k:
        clustered_df, centers = kmean_algorithm.run_kmeans(points_df.copy(), k)

        fig = go.Figure()

        cluster_colors = [
            "red", "green", "blue", "orange", "purple",
            "brown", "pink", "cyan", "lime", "gray"
        ]
        
        color_map = {i: cluster_colors[i % len(cluster_colors)] for i in range(k)}
        point_colors = clustered_df["cluster"].map(color_map)

        fig.add_trace(go.Scatter(
            x=clustered_df["X"],
            y=clustered_df["Y"],
            mode="markers",
            marker=dict(size=8, color=point_colors),
            name="Points",
            showlegend=False
        ))
        
        fig.add_trace(go.Scatter(
            x=centers[:, 0],
            y=centers[:, 1],
            mode="markers",
            marker=dict(symbol="x", size=12, color="black"),
            name="Centroids",
            showlegend=False
        ))

        fig.update_layout(
            width=PIXELS,
            height=PIXELS,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(range=[0, GRID_SIZE], title="X", fixedrange=True),
            yaxis=dict(range=[0, GRID_SIZE], title="Y", fixedrange=True, scaleanchor="x"),
        )

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("Click on canvas and select k ≥ 1 to visualize clusters.")

with col3:
    st.subheader("Clustered Data")
    if not points_df.empty:
        st.dataframe(points_df, use_container_width=True)
    else:
        st.warning("No points to show yet.")
