# Create docstring here
"""
This module contains unit tests for the Flask app.

It imports necessary libraries and functions for the application to work,
including Flask for web framework functionality,
rendering HTML templates, and handling HTTP requests. It also imports
functions from the 'model' module for image preprocessing and making predictions.

The application allows users to upload an image, preprocess it using the
'preprocess_img' function, and predict a result using the
'predict_result' function. The results are then displayed to the user.

Author: [Sec 2 – 5]
Date: [Current Date]
"""
import pytest
from flask.testing import FlaskClient
from PIL import UnidentifiedImageError, Image
from app import app

# Create a test client


@pytest.fixture
def test_client():
    """
    Create a test client for the Flask app.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the prediction route with a valid image


def test_predict_image_file_valid(test_client: FlaskClient, monkeypatch):
    """
    Test the prediction route with a valid image.
    """
    def mock_preprocess_img():
        # Mock preprocessing function
        return "MockImage"

    def mock_predict_result():
        # Mock prediction function
        return "MockResult"

    # Mock the functions from the 'model' module
    monkeypatch.setattr('model.preprocess_img', mock_preprocess_img)
    monkeypatch.setattr('model.predict_result', mock_predict_result)

    with open('Test_image.jpg', 'rb') as image_file:
        response = test_client.post(
            '/prediction', data={'file': (image_file, 'test_image.jpg')})

    assert response.status_code == 200
    # Check if "MockResult" is present in the rendered HTML response
    assert b"Successful" in response.data

# Test the prediction route with an invalid image that is not an image file


def test_predict_image_file_invalid_file(test_client: FlaskClient, monkeypatch):
    """
    Test the prediction route with an invalid image that is not an image file.
    """
    def mock_preprocess_img(img_stream):
        try:
            Image.open(img_stream)
        except UnidentifiedImageError as exc:
            raise ValueError("Invalid Image") from exc

    # Mock the function from the 'model' module
    monkeypatch.setattr('model.preprocess_img', mock_preprocess_img)

    # Create an invalid file, for example, a text file
    with open('Test.txt', 'w', encoding='utf-8') as invalid_file:
        invalid_file.write("This is not an image.")

    # Open the invalid text file for reading in binary mode with explicit encoding
    with open('Test.txt', 'rb') as image_file:
        with pytest.raises(UnidentifiedImageError):
            test_client.post(
                '/prediction', data={'file': (image_file, 'Test.txt')})


if __name__ == '__main__':
    pytest.main()
