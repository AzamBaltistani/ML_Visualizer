import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_drawable_canvas import st_canvas
from views.Regression import regression_models

st.set_page_config(page_title="Regression", layout="wide")
st.title("Interactive Regression Visualizer")

GRID_SIZE = 100
PIXELS = 400
CELL_SIZE = PIXELS // GRID_SIZE

if "clicked_points" not in st.session_state:
    st.session_state.clicked_points = []

# Dropdown for model type
model_type = st.selectbox("Select Regression Model", ["Linear Regression", "Polynomial Regression"])

col1, col2, col3 = st.columns([4, 4, 2], gap="small")

with col1:
    st.subheader("Input Panel (Click to add point)")
    canvas_result = st_canvas(
        fill_color="rgba(255, 0, 0, 0.7)",
        stroke_width=0,
        width=PIXELS,
        height=PIXELS,
        drawing_mode="point",
        update_streamlit=True,
        key="auto_canvas",
    )

with col2:
    st.subheader("Graph")

    if canvas_result.json_data and "objects" in canvas_result.json_data:
        new_points = []
        for obj in canvas_result.json_data["objects"]:
            x = int(obj["left"] // CELL_SIZE)
            y = GRID_SIZE - 1 - int(obj["top"] // CELL_SIZE)
            new_points.append((x, y))
        st.session_state.clicked_points = new_points

    df = pd.DataFrame(st.session_state.clicked_points, columns=["X", "Y"])

    if not df.empty:
        fig = go.Figure()

        # Scatter points
        fig.add_trace(go.Scatter(
            x=df["X"], y=df["Y"],
            mode="markers",
            marker=dict(color="red", size=6),
            showlegend=False
        ))

        regression_func = None
        equation = ""
        r2_score = None

        if len(df) >= 2:
            if model_type == "Linear Regression":
                regression_func, equation, r2_score = regression_models.linear_regression(df["X"], df["Y"])
            elif model_type == "Polynomial Regression":
                regression_func, equation, r2_score = regression_models.polynomial_regression(df["X"], df["Y"], degree=2)

            if regression_func:
                x_vals = list(range(0, GRID_SIZE + 1))
                y_vals = [regression_func(x) for x in x_vals]

                # Regression Line
                fig.add_trace(go.Scatter(
                    x=x_vals,
                    y=y_vals,
                    mode="lines",
                    line=dict(color="blue"),
                    showlegend=False
                ))

                # Absolute error lines
                for i, row in df.iterrows():
                    y_pred = regression_func(row["X"])
                    fig.add_trace(go.Scatter(
                        x=[row["X"], row["X"]],
                        y=[row["Y"], y_pred],
                        mode="lines",
                        line=dict(color="gray", dash="dot"),
                        showlegend=False
                    ))

        # Layout
        fig.update_layout(
            width=PIXELS,
            height=PIXELS,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(title="X", range=[0, 100], dtick=10, fixedrange=True),
            yaxis=dict(title="Y", range=[0, 100], dtick=10, fixedrange=True),
        )

        st.plotly_chart(fig, use_container_width=True)

        # Show R² score as a bar
        if r2_score is not None:
            st.markdown(f"**Model Equation:** ${equation}$")
            st.markdown(f"**R² Score:** {(r2_score.__round__(2))}")
            st.progress(min(max(r2_score, 0), 1))
    else:
        st.info("Click on the canvas to add points and see the graph.")

with col3:
    st.subheader("Points")
    df = pd.DataFrame(st.session_state.clicked_points, columns=["X", "Y"])
    st.dataframe(df, use_container_width=True)
    
with st.expander("See Regression Math Explanation"):
    with open("views/Regression/mathematics.md", "r") as f:
        st.markdown(f.read(), unsafe_allow_html=True)