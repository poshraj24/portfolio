import cv2
import numpy as np
from PIL import Image
import tensorflow as tf


def preprocess_image(img, target_size=(224, 224), grayscale=False):
    """
    Preprocess an image for ML model input.

    Args:
        img: Input image (numpy array or PIL Image)
        target_size: Tuple of (width, height) for resizing
        grayscale: Boolean, whether to convert to grayscale

    Returns:
        Preprocessed image as numpy array
    """
    # Convert PIL Image to numpy array if needed
    if isinstance(img, Image.Image):
        img = np.array(img)

    # Resize image
    if img.shape[0] != target_size[1] or img.shape[1] != target_size[0]:
        img = cv2.resize(img, target_size)

    # Convert to grayscale if requested
    if grayscale and len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.expand_dims(img, axis=-1)  # Add channel dimension

    # Normalize pixel values to [0, 1]
    img = img.astype(np.float32) / 255.0

    return img


def detect_faces(img, face_cascade):
    """
    Detect faces in an image using OpenCV cascade classifier.

    Args:
        img: Input image (numpy array)
        face_cascade: Loaded OpenCV CascadeClassifier

    Returns:
        List of tuples (x, y, w, h) for each detected face
    """
    # Convert to grayscale for face detection
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    return faces


def draw_faces(
    img, faces, predictions=None, labels=None, color=(0, 255, 0), thickness=2
):
    """
    Draw rectangles around detected faces with optional predictions.

    Args:
        img: Input image (numpy array)
        faces: List of face coordinates (x, y, w, h)
        predictions: Optional list of prediction indices
        labels: Optional list of label names
        color: BGR color tuple for rectangles
        thickness: Line thickness

    Returns:
        Image with drawn faces
    """
    result_img = img.copy()

    for i, (x, y, w, h) in enumerate(faces):
        # Draw rectangle
        cv2.rectangle(result_img, (x, y), (x + w, y + h), color, thickness)

        # Add prediction label if provided
        if predictions is not None and labels is not None:
            label = labels[predictions[i]]
            cv2.putText(
                result_img,
                label,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                color,
                thickness,
            )

    return result_img
