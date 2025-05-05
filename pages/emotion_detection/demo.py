import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import tensorflow as tf
from utils.image_processing import preprocess_image


# Load model only once
@st.cache_resource
def load_emotion_model():
    """Load the pre-trained emotion detection model."""
    model_path = os.path.join("models", "emotion_detection", "model.h5")
    model = tf.keras.models.load_model(model_path)
    return model


def show_emotion_detection():
    """Show the emotion detection demo interface."""
    st.subheader("Facial Emotion Detection")
    st.write(
        """
    This demo uses a deep learning model to detect emotions from facial expressions.
    The model can recognize 7 emotions: anger, disgust, fear, happiness, sadness, surprise, and neutral.
    """
    )

    # Load face detection cascade classifier
    face_cascade_path = os.path.join(
        "models", "emotion_detection", "haarcascade_frontalface_default.xml"
    )
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    # Load emotion detection model
    model = load_emotion_model()

    # Create tabs for different input methods
    tab1, tab2 = st.tabs(["Live Camera", "Upload Image"])

    with tab1:
        st.write("Allow camera access to detect emotions in real-time")
        img_file_buffer = st.camera_input("Take a picture")

        if img_file_buffer is not None:
            # Convert image to OpenCV format
            bytes_data = img_file_buffer.getvalue()
            img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

            # Process the image
            result_img, emotion = process_image(img, face_cascade, model)

            # Display result
            st.image(result_img, channels="BGR", use_column_width=True)

            # Change page theme based on emotion
            apply_theme_based_on_emotion(emotion)

    with tab2:
        uploaded_file = st.file_uploader(
            "Choose an image...", type=["jpg", "png", "jpeg"]
        )

        if uploaded_file is not None:
            # Convert image to OpenCV format
            image = Image.open(uploaded_file)
            img = np.array(image)

            # Process the image
            result_img, emotion = process_image(img, face_cascade, model)

            # Display result
            st.image(result_img, channels="BGR", use_column_width=True)

            # Change page theme based on emotion
            apply_theme_based_on_emotion(emotion)


def process_image(img, face_cascade, model):
    """Process the image to detect faces and emotions."""
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Create a copy of the image to draw on
    result_img = img.copy()

    # Default emotion if no face is detected
    emotion = "No face detected"

    # Process each face
    for x, y, w, h in faces:
        # Draw rectangle around face
        cv2.rectangle(result_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Extract face region
        face_img = gray[y : y + h, x : x + w]

        # Preprocess for model
        face_img = cv2.resize(face_img, (48, 48))
        face_img = np.expand_dims(face_img, axis=0)
        face_img = np.expand_dims(face_img, axis=-1)
        face_img = face_img / 255.0

        # Predict emotion
        emotion_labels = [
            "Angry",
            "Disgust",
            "Fear",
            "Happy",
            "Sad",
            "Surprise",
            "Neutral",
        ]
        emotion_pred = model.predict(face_img)
        emotion_idx = np.argmax(emotion_pred)
        emotion = emotion_labels[emotion_idx]

        # Display emotion on image
        cv2.putText(
            result_img,
            emotion,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )

    return result_img, emotion


def apply_theme_based_on_emotion(emotion):
    """Apply custom CSS based on detected emotion."""
    if emotion == "Happy":
        st.markdown(
            """
        <style>
        .stApp {
            background-color: #FFFACD;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
    elif emotion == "Sad":
        st.markdown(
            """
        <style>
        .stApp {
            background-color: #E6E6FA;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
    elif emotion == "Angry":
        st.markdown(
            """
        <style>
        .stApp {
            background-color: #FFE4E1;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )
    # Add more emotions and styles as needed
