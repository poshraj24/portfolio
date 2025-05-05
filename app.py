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

# Custom CSS with galaxy animation
st.markdown(
    """
<style>
/* Import Poppins font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Root variables */
:root {
    --primary-color: #6c63ff;
    --accent-color: #4cc9f0;
    --bg-color: #0f172a;
    --card-bg: rgba(30, 41, 59, 0.6);
    --text-color: #f8f9fa;
}

/* Main styling */
.stApp {
    background-color: var(--bg-color);
    background-image: 
        radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
        radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
        radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px);
    background-size: 550px 550px, 350px 350px, 250px 250px;
    background-position: 0 0, 40px 60px, 130px 270px;
    animation: galaxy-movement 120s linear infinite;
    color: var(--text-color);
}

@keyframes galaxy-movement {
    0% { background-position: 0 0, 40px 60px, 130px 270px; }
    100% { background-position: 1000px 1000px, 1040px 1060px, 1130px 1270px; }
}

/* Custom button styles */
.stButton > button {
    background: linear-gradient(45deg, var(--primary-color), var(--accent-color)) !important;
    color: white !important;
    border: none !important;
    padding: 10px 20px !important;
    border-radius: 8px !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3) !important;
}

/* Project cards */
.project-card {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    margin-bottom: 20px;
    backdrop-filter: blur(10px);
    border-left: 4px solid var(--primary-color);
}

.project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

/* Metrics styling */
.metric-container {
    background-color: var(--card-bg);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.metric-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
}

.metric-value {
    font-size: 24px;
    font-weight: bold;
    color: var(--primary-color);
}

.metric-label {
    font-size: 14px;
    opacity: 0.8;
}

/* Sidebar styling */
.css-1d391kg, .css-163ttbj {
    background-color: rgba(15, 23, 42, 0.8) !important;
    backdrop-filter: blur(10px) !important;
}

/* Make profile image round with a border */
.profile-img {
    border-radius: 50%;
    border: 3px solid var(--primary-color);
    box-shadow: 0 0 20px rgba(108, 99, 255, 0.5);
    transition: all 0.3s ease;
}

.profile-img:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(108, 99, 255, 0.7);
}

/* Animated gradient text */
.gradient-text {
    background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animated {
    animation: fadeIn 0.8s ease-out forwards;
}

/* Pill-shaped status indicator */
.status-indicator {
    display: inline-flex;
    align-items: center;
    background-color: rgba(76, 201, 240, 0.1);
    border: 1px solid var(--accent-color);
    border-radius: 20px;
    padding: 5px 12px;
    font-size: 14px;
}

.status-dot {
    width: 8px;
    height: 8px;
    background-color: #4CAF50;
    border-radius: 50%;
    margin-right: 8px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { opacity: 0.5; }
    50% { opacity: 1; }
    100% { opacity: 0.5; }
}

/* Fix text colors in various components */
.stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: var(--text-color) !important;
}

/* Custom divider */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent-color), transparent);
}

/* Hide default elements and navigation */
#MainMenu {visibility: hidden !important;}
footer {visibility: hidden !important;}
header {visibility: hidden !important;}
[data-testid="stSidebarNav"] {display: none !important;}

/* Top navigation styling */
.stButton button {
    border-radius: 10px !important;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2) !important;
}

/* Remove border from radio buttons in sidebar */
div.row-widget.stRadio > div [data-baseweb="radio"] input {
    display: none;
}

/* Fix html rendering in metrics */
div.stMetric {
    background-color: var(--card-bg) !important;
    border-radius: 12px !important;
    padding: 15px !important;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15) !important;
}

div.stMetric label {
    color: var(--text-color) !important;
    opacity: 0.8 !important;
}

div.stMetric .metric-value {
    color: var(--primary-color) !important;
    font-weight: bold !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Create functional top navigation
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home", key="nav_home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with col2:
    if st.button("💻 Projects", key="nav_projects", use_container_width=True):
        st.session_state.page = "Projects"
        st.rerun()

with col3:
    if st.button("📊 Skills", key="nav_skills", use_container_width=True):
        st.session_state.page = "Skills & Experience"
        st.rerun()

with col4:
    if st.button("🧠 ML Demo", key="nav_demo", use_container_width=True):
        st.session_state.page = "ML Demo"
        st.rerun()

with col5:
    if st.button("✉️ Contact", key="nav_contact", use_container_width=True):
        st.session_state.page = "Contact"
        st.rerun()

# Add separator
st.markdown(
    "<hr style='margin: 0.5rem 0 1.5rem 0; opacity: 0.2;'>", unsafe_allow_html=True
)

# Call sidebar function (only for profile and social links, not navigation)
show_sidebar()

# Display the selected page based on session state
if st.session_state.page == "Home":
    show_home()
elif st.session_state.page == "Projects":
    show_projects()
elif st.session_state.page == "Skills & Experience":
    show_skills()
elif st.session_state.page == "ML Demo":
    show_ml_demo()
elif st.session_state.page == "Contact":
    show_contact()
