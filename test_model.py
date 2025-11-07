"""
test_model.py

Unit tests for the image classification model functions:
- preprocess_img
- predict_result
"""

import pytest
import numpy as np
from keras.models import load_model
from model import preprocess_img, predict_result

# Load the model once for all tests
@pytest.fixture(scope="module")
def loaded_model():
    """Load the model once for all tests."""
    return load_model("digit_model.h5")  # Adjust path as needed


# Basic Tests


def test_preprocess_img():
    """Test the preprocess_img function."""
    img_path = "test_images/2/Sign 2 (97).jpeg"
    processed_img = preprocess_img(img_path)

    assert processed_img.shape == (1, 224, 224, 3), \
        "Processed image shape should be (1, 224, 224, 3)"
    assert 0 <= np.min(processed_img) <= 1 and 0 <= np.max(processed_img) <= 1, \
        "Image pixel values should be normalized between 0 and 1"


def test_predict_result(loaded_model):
    """Test the predict_result function."""
    img_path = "test_images/4/Sign 4 (92).jpeg"
    processed_img = preprocess_img(img_path)

    prediction = predict_result(processed_img)
    assert isinstance(prediction, (int, np.integer)), \
        "Prediction should be an integer class index"

# Advanced Tests

def test_invalid_image_path():
    """Test preprocess_img with an invalid image path."""
    with pytest.raises(FileNotFoundError):
        preprocess_img("invalid/path/to/image.jpeg")


def test_image_shape_on_prediction(loaded_model):
    """Test that the prediction output is an integer."""
    img_path = "test_images/5/Sign 5 (86).jpeg"
    processed_img = preprocess_img(img_path)

    prediction = predict_result(processed_img)
    assert isinstance(prediction, (int, np.integer)), \
        "The prediction should be an integer"


def test_model_predictions_consistency(loaded_model):
    """Test that predictions for the same input are consistent."""
    img_path = "test_images/7/Sign 7 (54).jpeg"
    processed_img = preprocess_img(img_path)

    predictions = [predict_result(processed_img) for _ in range(5)]
    assert all(p == predictions[0] for p in predictions), \
        "Predictions for the same input should be consistent"
