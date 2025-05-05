import streamlit as st


def show_sidebar():
    """Display the sidebar with profile information and languages (no navigation)."""
    # Profile image with rounded styling
    st.sidebar.image("assets/images/profile.jpg", width=150, use_column_width=False)
    st.sidebar.title("Posh Raj Dahal")
    st.sidebar.write("Data Scientist | ML Engineer")

    # Social icons using Unicode emoji (more reliable than image files)
    st.sidebar.markdown(
        """
    <div style="display: flex; justify-content: space-around; margin-top: 10px; margin-bottom: 20px;">
        <a href="https://linkedin.com/in/poshrajdahal" target="_blank" style="text-decoration: none; font-size: 24px;">
            🔗
        </a>
        <a href="https://github.com/poshraj24" target="_blank" style="text-decoration: none; font-size: 24px;">
            💻
        </a>
        <a href="mailto:dahal.poshraj24@gmail.com" style="text-decoration: none; font-size: 24px;">
            ✉️
        </a>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Languages section (keeping this part)
    st.sidebar.markdown("## Languages")
    st.sidebar.markdown("- German (B1)")
    st.sidebar.markdown("- English (Fluent)")
    st.sidebar.markdown("- Nepali (Native)")

    # Status indicator
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
    <div style="display: flex; align-items: center; background-color: rgba(76, 201, 240, 0.1); 
         border-radius: 20px; padding: 8px 15px; border: 1px solid #4cc9f0;">
        <div style="width: 8px; height: 8px; background-color: #4CAF50; border-radius: 50%; 
             margin-right: 8px; animation: pulse 2s infinite;"></div>
        <span>Available for opportunities</span>
    </div>
    <style>
    @keyframes pulse {
        0% { opacity: 0.5; }
        50% { opacity: 1; }
        100% { opacity: 0.5; }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # No need to return a selected page since navigation is handled through the top bar
    return None
