import streamlit as st
from app.pages import weight_loss, diabetes_management, muscle_building

# Page navigation
PAGES = {
    "Weight Loss Journey": weight_loss,
    "Managing Diabetes": diabetes_management,
    "Building Muscle": muscle_building,
}

st.sidebar.title("Nutritionist AI")
choice = st.sidebar.radio("Navigate to:", list(PAGES.keys()))
page = PAGES[choice]
page.run()
