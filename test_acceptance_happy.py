"""
test_acceptance_happy.py

This module contains acceptance tests for the happy path scenarios of the
Flask image prediction application. The tests cover:

1. Uploading a valid image file
2. Uploading large but valid image files
3. Uploading images with a specific large size or resolution

Each test ensures the application handles these scenarios correctly and
returns valid prediction responses.
"""

from io import BytesIO
from unittest.mock import patch, MagicMock


with patch("tensorflow.keras.models.load_model") as mock_load_model:
    mock_model = MagicMock()
    mock_model.predict.return_value = [[0.1, 0.9]]  
    mock_load_model.return_value = mock_model

    from app import app

import pytest

@pytest.fixture
def _client():
    with app.test_client() as client:
        yield client

def _post_image(_client, img_bytes, filename):
    """
    Helper function to post an image to the /prediction endpoint.
    """
    img_data = BytesIO(img_bytes)
    img_data.name = filename
    response = _client.post(
        "/prediction",
        data={"file": (img_data, filename)},
        content_type="multipart/form-data"
    )
    return response

def test_acceptance_successful_upload(_client):
    """
    Test Case: Successful Upload of a Valid Image File
    - Purpose: Ensure the application accepts a valid image file upload and provides a prediction.
    """
    response = _post_image(_client, b"fake_image_data", "test_image.jpg")
    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_acceptance_valid_large_image(_client):
    """
    Test Case: Upload of a Valid Large Image File
    - Purpose: Check if the system accepts large but valid image files without errors and still provides predictions.
    """
    large_image_bytes = b"fake_large_image_data" * 1000  
    response = _post_image(_client, large_image_bytes, "large_image.jpg")
    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_acceptance_valid_image_size_upload(_client):
    """
    Test Case: Upload of an Image with a Specific Large Size
    - Purpose: Validate system behavior with valid image files of a specific size or resolution.
    """
    large_size_bytes = b"valid_image_data_of_large_size" * 1000  
    response = _post_image(_client, large_size_bytes, "large_image.jpg")
    assert response.status_code == 200
    assert b"Prediction" in response.data