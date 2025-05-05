import streamlit as st


def show_sidebar():
    """Display the sidebar navigation and return the selected page."""
    st.sidebar.image("assets/images/profile.jpg", width=150)
    st.sidebar.title("Posh Raj Dahal")
    st.sidebar.write("Data Scientist | ML Engineer")

    # Add links to social profiles
    cols = st.sidebar.columns(3)
    with cols[0]:
        st.markdown(
            "[![LinkedIn](assets/images/icons/linkedin.png)](https://linkedin.com/in/poshrajdahal)"
        )
    with cols[1]:
        st.markdown(
            "[![GitHub](assets/images/icons/github.png)](https://github.com/poshraj24)"
        )
    with cols[2]:
        st.markdown(
            "[![Email](assets/images/icons/email.png)](mailto:dahal.poshraj24@gmail.com)"
        )

    # Navigation menu
    st.sidebar.markdown("## Navigation")

    selected_page = st.sidebar.radio(
        "",
        ["Home", "Projects", "Skills & Experience", "ML Demo", "Contact"],
        label_visibility="collapsed",
    )

    # Additional sidebar content
    st.sidebar.markdown("---")
    st.sidebar.markdown("## Languages")
    st.sidebar.markdown("- German (B1)")
    st.sidebar.markdown("- English (Fluent)")
    st.sidebar.markdown("- Nepali (Native)")

    return selected_page
