import streamlit as st

st.title("ML Model Visualizer ")
st.subheader("Explore any interactive playground", anchor=False)

st.write("## 1. Interactive Linear Regression Visualizer")
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.write("**Linear Regression Demo**")
    st.image("views/images/linear_reg.gif", use_container_width=True)
        
with col2:
    st.write("**Polynomial Regression Demo**")
    st.image("views/images/poly_reg.gif", use_container_width=True)

linearReg_btn = st.button("Goto Playground", key="linear_reg_btn")
if linearReg_btn:
    st.switch_page("views/Regression/user_interface.py")
    
st.write("## 2. Interactive K-Mean Visualizer")
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.write("**K-Mean Clustering Demo**")
    st.image("views/images/kmeans_1.gif", use_container_width=True)

with col2:
    st.write("**K-Mean Clustering Demo**")
    st.image("views/images/kmeans_2.gif", use_container_width=True)

kmeans_btn = st.button("Goto Playground", key="kmeans_btn")
if kmeans_btn:
    st.switch_page("views/KMeans/user_interface.py")