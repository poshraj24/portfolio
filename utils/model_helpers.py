import tensorflow as tf
import numpy as np
import os
import streamlit as st


@st.cache_resource
def load_model(model_path):
    """
    Load a TensorFlow/Keras model with caching.

    Args:
        model_path: Path to the model file

    Returns:
        Loaded model
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")


def predict_single(model, input_data, preprocess_func=None):
    """
    Make prediction for a single input.

    Args:
        model: Loaded ML model
        input_data: Input data (image, text, etc.)
        preprocess_func: Optional preprocessing function

    Returns:
        Prediction result
    """
    # Apply preprocessing if provided
    if preprocess_func:
        input_data = preprocess_func(input_data)

    # Ensure input is in batch format
    if len(input_data.shape) == 3:  # For images with shape (h, w, c)
        input_data = np.expand_dims(input_data, axis=0)

    # Make prediction
    try:
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        raise Exception(f"Prediction error: {str(e)}")


def get_prediction_class(prediction, labels, top_k=1):
    """
    Get class label(s) from model prediction.

    Args:
        prediction: Model prediction output
        labels: List of class labels
        top_k: Number of top predictions to return

    Returns:
        List of (label, probability) tuples
    """
    # For single-class predictions
    if len(prediction.shape) == 2:  # (batch_size, num_classes)
        # Get indices of top k predictions
        indices = np.argsort(prediction[0])[::-1][:top_k]

        # Get labels and probabilities
        result = [(labels[idx], float(prediction[0][idx])) for idx in indices]

        return result
    else:
        # For other prediction types (e.g., regression)
        return prediction
