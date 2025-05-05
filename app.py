import streamlit as st
from pages.home import show_home
from pages.projects import show_projects
from pages.skills import show_skills
from pages.ml_demo import show_ml_demo
from pages.contact import show_contact
from components.sidebar import show_sidebar

# Configure page settings
st.set_page_config(
    page_title="Posh Raj Dahal | Data Scientist & ML Engineer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
with open("assets/css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Show sidebar
selected_page = show_sidebar()

# Display the selected page
if selected_page == "Home":
    show_home()
elif selected_page == "Skills & Experience":
    show_skills()
elif selected_page == "ML Demo":
    show_ml_demo()
elif selected_page == "Contact":
    show_contact()
