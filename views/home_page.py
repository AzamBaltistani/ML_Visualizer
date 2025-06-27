import streamlit as st

st.title("ML Model Visulizer ")
st.subheader("All models are built from scratch without using any Libary just Math :)", anchor=False)

st.write("## 1. Interactive Linear Regression Visualizer")
linearReg_btn = st.button("Goto Playground")
if linearReg_btn:
    st.switch_page("views/Regression/user_interface.py")