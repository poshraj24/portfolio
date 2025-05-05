"""
Configuration settings for the portfolio application.
"""

# Application settings
APP_TITLE = "Posh Raj Dahal | Data Scientist & ML Engineer"
APP_ICON = "📊"
DEFAULT_LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# File paths
PROFILE_IMAGE_PATH = "assets/images/profile.jpg"
MODELS_DIR = "models"
DATA_DIR = "assets/data"

# ML Model settings
EMOTION_DETECTION = {
    "model_path": "models/emotion_detection/model.h5",
    "cascade_path": "models/emotion_detection/haarcascade_frontalface_default.xml",
    "labels": ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"],
    "input_shape": (48, 48, 1),
}

COVID_DETECTION = {
    "model_path": "models/covid_detection/model.h5",
    "input_shape": (224, 224, 3),
    "labels": ["Normal", "COVID-19", "Viral Pneumonia"],
}

TRANSLATION = {
    "model_path": "models/translation/model.h5",
    "source_lang": "Nepali",
    "target_lang": "German",
}

# Contact form settings
EMAIL_RECEIVER = "dahal.poshraj24@gmail.com"
CONTACT_FORM_SUBJECT = "Portfolio Website Contact"

# Theme settings
THEME_COLORS = {
    "Happy": "#FFFACD",
    "Sad": "#E6E6FA",
    "Angry": "#FFE4E1",
    "Neutral": "#FFFFFF",
    "Surprise": "#E0FFFF",
    "Fear": "#F5F5F5",
    "Disgust": "#F0FFF0",
}

# Project links
PROJECT_LINKS = {
    "gene_network": "https://github.com/poshraj24/gene-regulatory-kan",
    "covid_detection": "https://github.com/poshraj24/covid-detection",
    "translation": "https://github.com/poshraj24/nepali-german-translation",
    "climate_analysis": "https://github.com/poshraj24/climate-analysis",
    "finance_ml": "https://github.com/poshraj24/finance-ml",
}
