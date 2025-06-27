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

linearReg_btn = st.button("Goto Playground")
if linearReg_btn:
    st.switch_page("views/Regression/user_interface.py")