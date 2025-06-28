import streamlit as st

st.set_page_config(
    layout="wide"
)

pages = st.navigation(
    [
        st.Page(
            page="views/home_page.py",
            title="ML Visualizer",
            default=True
        ),
        st.Page(
            page="views/Regression/user_interface.py",
            title="Regression",
            url_path="regression"
        ),
        st.Page(
            page="views/KMeans/user_interface.py",
            title="K-Means",
            url_path="kmeans"
        )
    ]
)

pages.run()