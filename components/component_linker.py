import streamlit as st


def create_top_navigation():
    """Create top navigation bar links that set session state."""

    # Create a horizontal container for the top links
    cols = st.columns(6)

    with cols[0]:
        if st.button("Home", key="nav_home", use_container_width=True):
            st.session_state["navigation"] = "Home"
            st.rerun()  # Changed from experimental_rerun

    with cols[1]:
        if st.button("Projects", key="nav_projects", use_container_width=True):
            st.session_state["navigation"] = "Projects"
            st.rerun()  # Changed from experimental_rerun

    with cols[2]:
        if st.button("Skills", key="nav_skills", use_container_width=True):
            st.session_state["navigation"] = "Skills & Experience"
            st.rerun()  # Changed from experimental_rerun

    with cols[3]:
        if st.button("ML Demo", key="nav_demo", use_container_width=True):
            st.session_state["navigation"] = "ML Demo"
            st.rerun()  # Changed from experimental_rerun

    with cols[4]:
        if st.button("Contact", key="nav_contact", use_container_width=True):
            st.session_state["navigation"] = "Contact"
            st.rerun()  # Changed from experimental_rerun
