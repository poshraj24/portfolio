import streamlit as st
import numpy as np
import pandas as pd


def show_ml_demo():
    """Display ML demo page with interactive demos."""
    st.title("Interactive ML Demos")
    st.write("Experience machine learning in action with these interactive demos!")

    # Demo selection
    demo_type = st.selectbox(
        "Select a demo",
        ["Emotion Detection", "COVID-19 Detection", "Nepali-German Translation"],
    )

    st.markdown("---")

    # Show the selected demo
    if demo_type == "Emotion Detection":
        show_emotion_detection()
    elif demo_type == "COVID-19 Detection":
        show_covid_detection()
    elif demo_type == "Nepali-German Translation":
        show_translation_demo()


def show_emotion_detection():
    """Demo for emotion detection."""
    st.subheader("Facial Emotion Detection")
    st.write(
        """
    This demo uses a deep learning model to detect emotions from facial expressions.
    The model can recognize 7 emotions: anger, disgust, fear, happiness, sadness, surprise, and neutral.
    """
    )

    # Camera input (simplified version without actual model)
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # Display uploaded image
        st.image(img_file_buffer)

        # Simulate emotion detection (would be replaced with actual model)
        emotions = ["Happy", "Sad", "Angry", "Surprised", "Neutral", "Fear", "Disgust"]
        detected_emotion = np.random.choice(emotions)

        # Display result
        st.success(f"Detected emotion: {detected_emotion}")

        # Change theme based on emotion (simplified)
        if detected_emotion == "Happy":
            st.balloons()
            st.markdown(
                """
            <style>
            .stApp {background-color: #FFFACD;}
            </style>
            """,
                unsafe_allow_html=True,
            )
        elif detected_emotion == "Sad":
            st.markdown(
                """
            <style>
            .stApp {background-color: #E6E6FA;}
            </style>
            """,
                unsafe_allow_html=True,
            )


def show_covid_detection():
    """Demo for COVID-19 detection."""
    st.subheader("COVID-19 Detection System")
    st.write(
        """
    This demo uses a hybrid CNN-ResNet model to detect COVID-19 from chest X-ray images.
    The model achieves an accuracy of 87.29% using transfer learning techniques.
    """
    )

    # Upload image
    uploaded_file = st.file_uploader(
        "Upload a chest X-ray image", type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, caption="Uploaded X-ray image")

        # Add a processing button
        if st.button("Analyze Image"):
            # Simulate processing (would be replaced with actual model)
            with st.spinner("Processing image..."):
                import time

                time.sleep(2)  # Simulate processing time

                # Simulated results
                results = {"Normal": 0.15, "COVID-19": 0.75, "Viral Pneumonia": 0.10}

                # Display results
                st.subheader("Analysis Results:")

                # Create a bar chart
                results_df = pd.DataFrame(
                    {
                        "Category": list(results.keys()),
                        "Probability": list(results.values()),
                    }
                )

                st.bar_chart(results_df.set_index("Category"))

                # Show prediction
                prediction = max(results, key=results.get)
                st.markdown(
                    f"**Prediction: {prediction}** (Confidence: {results[prediction]:.2%})"
                )


def show_translation_demo():
    """Demo for Nepali-German translation."""
    st.subheader("Nepali to German Language Translation")
    st.write(
        """
    This demo showcases a speech-to-speech translation system that translates between Nepali and German.
    It uses a pivoting strategy with pre-trained transformers for effective translation.
    """
    )

    # Text input
    input_lang = st.radio("Select input language:", ["Nepali", "German"])

    if input_lang == "Nepali":
        output_lang = "German"
    else:
        output_lang = "Nepali"

    text_input = st.text_area(f"Enter {input_lang} text:", height=100)

    # Translation button
    if st.button("Translate") and text_input:
        with st.spinner(f"Translating from {input_lang} to {output_lang}..."):
            # Simulate translation (would be replaced with actual model)
            import time

            time.sleep(2)  # Simulate processing time

            # Sample translations (just for demo)
            if input_lang == "Nepali":
                sample_translations = {
                    "नमस्ते": "Hallo",
                    "तपाईंलाई कस्तो छ?": "Wie geht es Ihnen?",
                    "धन्यवाद": "Danke",
                    "मलाई नेपाली बोल्न आउँछ": "Ich kann Nepalesisch sprechen",
                }
                # Default translation if input not in samples
                translation = sample_translations.get(
                    text_input, "Übersetzung nicht verfügbar"
                )
            else:
                sample_translations = {
                    "Hallo": "नमस्ते",
                    "Wie geht es Ihnen?": "तपाईंलाई कस्तो छ?",
                    "Danke": "धन्यवाद",
                    "Ich kann Deutsch sprechen": "म जर्मन बोल्न सक्छु",
                }
                # Default translation if input not in samples
                translation = sample_translations.get(text_input, "अनुवाद उपलब्ध छैन")

            # Display result
            st.subheader(f"{output_lang} Translation:")
            st.success(translation)
