import streamlit as st


def show_home():
    """Display the homepage content."""
    # Hero section
    st.title("Posh Raj Dahal")
    st.subheader("Data Scientist & Machine Learning Engineer")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            """
        ## Welcome to my portfolio!
        
        I'm a Machine Learning Engineer with expertise in deep learning, computer vision,
        and natural language processing. Currently pursuing my MSc in Data Science at 
        FAU Erlangen-Nuremberg, Germany.
        
        My work focuses on developing innovative ML solutions, from gene regulatory networks 
        to language translation systems.
        
        ### Featured Project: Emotion Detection
        Try out the live emotion detection demo in the ML Demo section!
        """
        )

        # Call-to-action buttons
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            st.button("View Projects", use_container_width=True)
        with col_btn2:
            st.button("Try ML Demo", use_container_width=True)

    with col2:
        # Stats/highlights
        st.markdown("### At a Glance")
        st.metric(label="ML Projects", value="8+")
        st.metric(label="Years Experience", value="4+")
        st.metric(label="Frameworks", value="PyTorch, TensorFlow")

    # Brief project highlights
    st.markdown("---")
    st.markdown("## Recent Projects")

    # Project cards in 3 columns
    cols = st.columns(3)

    with cols[0]:
        st.markdown("### Gene-regulatory Networks")
        st.markdown("Novel approach using Kolmogorov-Arnold Networks")

    with cols[1]:
        st.markdown("### Nepali-German Translation")
        st.markdown("Speech-to-speech translation using transformers")

    with cols[2]:
        st.markdown("### COVID-19 Detection")
        st.markdown("Hybrid CNN-ResNet model with 87.29% accuracy")
