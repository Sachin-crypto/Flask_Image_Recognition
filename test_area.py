import os
import io
import pytest
from flask import Flask
from flask.testing import FlaskClient
from model import preprocess_img, predict_result
from app import app
import PIL
from PIL import UnidentifiedImageError, Image
# Create a test client


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test the prediction route with a valid image


def test_predict_image_file_valid(client: FlaskClient, monkeypatch):
    def mock_preprocess_img(img_stream):
        # Mock preprocessing function
        return "MockImage"

    def mock_predict_result(img):
        # Mock prediction function
        return "MockResult"

    # Mock the functions from the 'model' module
    monkeypatch.setattr('model.preprocess_img', mock_preprocess_img)
    monkeypatch.setattr('model.predict_result', mock_predict_result)

    with open('Test_image.jpg', 'rb') as image_file:
        response = client.post(
            '/prediction', data={'file': (image_file, 'test_image.jpg')})

    assert response.status_code == 200
    # Check if "MockResult" is present in the rendered HTML response
    assert b"Successfull" in response.data
