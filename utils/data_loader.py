import pandas as pd
import numpy as np
import os
import json
import streamlit as st


@st.cache_data
def load_csv_data(filepath):
    """
    Load CSV data with caching.

    Args:
        filepath: Path to the CSV file

    Returns:
        Pandas DataFrame
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        raise Exception(f"Error loading CSV data: {str(e)}")


@st.cache_data
def load_json_data(filepath):
    """
    Load JSON data with caching.

    Args:
        filepath: Path to the JSON file

    Returns:
        Loaded JSON data
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"JSON file not found: {filepath}")

    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise Exception(f"Error loading JSON data: {str(e)}")


def load_sample_images(directory, limit=10):
    """
    Load sample images from a directory.

    Args:
        directory: Path to image directory
        limit: Maximum number of images to load

    Returns:
        List of image file paths
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

    # Get all image files in directory
    image_files = []
    for file in os.listdir(directory):
        ext = os.path.splitext(file)[1].lower()
        if ext in image_extensions:
            image_files.append(os.path.join(directory, file))

    # Limit the number of files
    if limit > 0 and len(image_files) > limit:
        image_files = image_files[:limit]

    return image_files


def load_project_metadata():
    """
    Load metadata for all projects.

    Returns:
        Dictionary of project metadata
    """
    # This would typically load from a JSON file, but for this example,
    # we'll create it directly
    projects = {
        "gene_network": {
            "title": "Gene-regulatory Kolmogorov-Arnold Networks",
            "description": "Developing a novel approach to model gene regulatory networks using Kolmogorov-Arnold Networks (KANs), focusing on capturing higher-order effects between regulatory genes.",
            "image": "assets/images/projects/gene_network.jpg",
            "technologies": ["Python", "PyTorch", "UNIX"],
            "date": "October 2024 - Present",
        },
        "nepali_german": {
            "title": "Nepali to German Language Translation",
            "description": "Developed speech-to-speech translation system using pivoting strategy with pre-trained transformers.",
            "image": "assets/images/projects/translation.jpg",
            "technologies": ["Flutter", "PyTorch", "NLTK", "NumPy", "Google Colab"],
            "date": "August 2024 - Present",
        },
        "covid_detection": {
            "title": "COVID-19 Detection System",
            "description": "Built hybrid CNN-ResNet model achieving 87.29% accuracy using transfer learning.",
            "image": "assets/images/projects/covid.jpg",
            "technologies": ["PyTorch", "TensorFlow", "Keras"],
            "date": "September 2024",
        },
        "gene_set": {
            "title": "Gene Set Enrichment Analysis",
            "description": "Conducted bioinformatics analysis using Mann-Whitney U test with multiple corrections.",
            "image": "assets/images/projects/gene_set.jpg",
            "technologies": ["Python", "Pandas", "Statistical Analysis"],
            "date": "July 2024",
        },
        "climate": {
            "title": "Climate Related Issues Analysis",
            "description": "Using a CI/CD data engineering pipeline, a prediction tool was developed to find the correlation between CO2 emissions and frequencies of climate-related disasters.",
            "image": "assets/images/projects/climate.jpg",
            "technologies": ["Jayvee", "Python"],
            "date": "April 2024",
        },
    }

    return projects
