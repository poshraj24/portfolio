import streamlit as st


def show_home():
    """Display the homepage with proper metrics and styling."""

    # Hero section with gradient text
    st.markdown(
        """
    <h1 class="gradient-text" style="font-size: 2.8rem; margin-bottom: 0.2rem;">Posh Raj Dahal</h1>
    <h2 style="margin-top: 0; opacity: 0.9; font-size: 1.8rem;">Data Scientist & Machine Learning Engineer</h2>
    """,
        unsafe_allow_html=True,
    )

    # Main content in two columns
    col1, col2 = st.columns([2, 1])

    # with col1:
    #     st.markdown(
    #         """
    #     <div style="animation: fadeIn 0.8s ease-out 0.2s forwards;">
    #         <h2 style="margin-top: 0.5rem;">Welcome to my portfolio!</h2>
    #         <p>I'm a Machine Learning Engineer with expertise in deep learning, computer vision,
    #         and natural language processing. Currently pursuing my MSc in Data Science at
    #         FAU Erlangen-Nuremberg, Germany.</p>

    #         <p>My work focuses on developing innovative ML solutions, from gene regulatory networks
    #         to language translation systems.</p>

    #         <h3>Featured Project: Emotion Detection</h3>
    #         <p>Try out the live emotion detection demo in the ML Demo section!</p>
    #     </div>
    #     """,
    #         unsafe_allow_html=True,
    # #     )

    #     # Call-to-action buttons using native Streamlit buttons
    #     btn_col1, btn_col2 = st.columns(2)
    #     with btn_col1:
    #         if st.button(
    #             "View Projects", key="btn_view_projects", use_container_width=True
    #         ):
    #             st.session_state.page = "Projects"
    #             st.rerun()

    #     with btn_col2:
    #         if st.button(
    #             "Try ML Demo", key="btn_try_ml_demo", use_container_width=True
    #         ):
    #             st.session_state.page = "ML Demo"
    #             st.rerun()
    with col1:
        st.subheader("Welcome to my portfolio!")

        st.write(
            """
            I'm a **Machine Learning Engineer** with expertise in deep learning, computer vision, 
            and natural language processing. I'm currently pursuing my MSc in Data Science at 
            **FAU Erlangen-Nuremberg, Germany**.

            My work focuses on developing innovative ML solutions — from **gene regulatory networks** 
            to **language translation systems**.
            """
        )

        st.markdown("### 🎯 Featured Project: Emotion Detection")
        st.write("Try out the live emotion detection demo in the **ML Demo** section!")

        # Call-to-action buttons
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button(
                "View Projects", key="btn_view_projects", use_container_width=True
            ):
                st.session_state.page = "Projects"
                st.rerun()

        with btn_col2:
            if st.button(
                "Try ML Demo", key="btn_try_ml_demo", use_container_width=True
            ):
                st.session_state.page = "ML Demo"
                st.rerun()

    with col2:
        # Use native Streamlit metrics instead of custom HTML
        st.markdown("<h3>At a Glance</h3>", unsafe_allow_html=True)

        # Native Streamlit metrics
        st.metric(label="ML Projects", value="8+")
        st.metric(label="Years Experience", value="4+")
        st.metric(label="Frameworks", value="PyTorch, TensorFlow")

    # Recent projects section
    st.markdown("<hr style='margin: 2rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
    st.markdown("<h2>Recent Projects</h2>", unsafe_allow_html=True)

    # Project cards in 3 columns
    proj_col1, proj_col2, proj_col3 = st.columns(3)

    with proj_col1:
        st.markdown(
            """
        <div class="project-card">
            <h3>🧬 Gene-regulatory Networks</h3>
            <p>Novel approach using Kolmogorov-Arnold Networks</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("Learn More", key="btn_learn_more_1", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()

    with proj_col2:
        st.markdown(
            """
        <div class="project-card">
            <h3>🌍 Nepali-German Translation</h3>
            <p>Speech-to-speech translation using transformers</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("Learn More", key="btn_learn_more_2", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()

    with proj_col3:
        st.markdown(
            """
        <div class="project-card">
            <h3>🦠 COVID-19 Detection</h3>
            <p>Hybrid CNN-ResNet model with 87.29% accuracy</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("Learn More", key="btn_learn_more_3", use_container_width=True):
            st.session_state.page = "Projects"
            st.rerun()
