import streamlit as st


def show_header(title=None):
    """Display the header component."""
    with st.container():
        st.markdown('<div class="header-container">', unsafe_allow_html=True)

        # Logo and title area
        cols = st.columns([1, 3])
        with cols[0]:
            st.image("assets/images/logo.png", width=80)
        with cols[1]:
            if title:
                st.title(title)
            else:
                st.title("Posh Raj Dahal | Data Scientist")

        st.markdown("</div>", unsafe_allow_html=True)

        # Optional: Add a horizontal divider
        st.markdown("---")
