import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_drawable_canvas import st_canvas
from views.DBSCAN import dbscan_model

st.set_page_config(page_title="DBSCAN Visualizer", layout="wide")
st.title("DBSCAN Clustering Visualizer")

GRID_SIZE = 100
PIXELS = 400
CELL_SIZE = PIXELS // GRID_SIZE

if "dbscan_points" not in st.session_state:
    st.session_state.dbscan_points = []

col1, col2, col3 = st.columns([4, 4, 2], gap="small")

with col1:
    st.subheader("Input & Parameters")

    canvas_result = st_canvas(
        fill_color="rgba(0, 100, 200, 0.6)",
        stroke_width=0,
        width=PIXELS,
        height=PIXELS,
        drawing_mode="point",
        update_streamlit=True,
        key="dbscan_canvas",
    )

    if canvas_result.json_data and "objects" in canvas_result.json_data:
        new_points = []
        for obj in canvas_result.json_data["objects"]:
            x = int(obj["left"] // CELL_SIZE)
            y = GRID_SIZE - 1 - int(obj["top"] // CELL_SIZE)
            new_points.append((x, y))
        st.session_state.dbscan_points = new_points

    eps = st.slider("Epsilon (eps)", 1.0, 20.0, 5.0, step=0.5)
    min_samples = st.slider("Min Samples", 1, 10, 3)

with col2:
    st.subheader("DBSCAN Clusters")

    points_df = pd.DataFrame(st.session_state.dbscan_points, columns=["X", "Y"])

    if not points_df.empty:
        clustered_df, n_clusters = dbscan_model.run_dbscan(points_df.copy(), eps, min_samples)

        cluster_colors = [
            "red", "green", "blue", "orange", "purple",
            "brown", "pink", "cyan", "lime", "gray"
        ]
        color_map = {i: cluster_colors[i % len(cluster_colors)] for i in clustered_df["cluster"].unique() if i != -1}
        point_colors = clustered_df["cluster"].map(lambda c: "black" if c == -1 else color_map[c])

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=clustered_df["X"],
            y=clustered_df["Y"],
            mode="markers",
            marker=dict(size=8, color=point_colors),
            name="Points",
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
        st.info("Click on canvas to add points.")

with col3:
    st.subheader("Clustered Data")
    if not points_df.empty:
        st.dataframe(points_df, use_container_width=True)
    else:
        st.warning("No points available.")
