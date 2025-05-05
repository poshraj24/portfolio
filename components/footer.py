import streamlit as st


def show_footer():
    """Display the footer component."""
    st.markdown("---")
    with st.container():
        st.markdown('<div class="footer-container">', unsafe_allow_html=True)

        cols = st.columns(3)

        with cols[0]:
            st.markdown("**Contact**")
            st.markdown("📧 dahal.poshraj24@gmail.com")
            st.markdown("📱 +49 17610815381")

        with cols[1]:
            st.markdown("**Location**")
            st.markdown("Erlangen, Germany")

        with cols[2]:
            st.markdown("**Connect**")
            st.markdown(
                "[![LinkedIn](assets/images/icons/linkedin-small.png)](https://linkedin.com/in/poshrajdahal)"
            )
            st.markdown(
                "[![GitHub](assets/images/icons/github-small.png)](https://github.com/poshraj24)"
            )

        # Copyright
        st.markdown("© 2025 Posh Raj Dahal. All rights reserved.")
        st.markdown("</div>", unsafe_allow_html=True)
