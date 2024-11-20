# test_acceptance_happy.py

from io import BytesIO
import pytest

def test_acceptance_successful_upload(client):
    """Test acceptance of a valid image file upload and receiving a prediction."""
    # Create a mock image file with minimal valid content.
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test_image.jpg"

    # Simulate the file upload to the prediction route
    response = client.post(
        "/prediction",  # The route for prediction
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Assertions: Check if the status code is 200 and "Prediction" is in the response data
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Modify this check based on the actual prediction content

def test_acceptance_valid_large_image(client):
    """Test acceptance of a valid large image file upload and receiving a prediction."""
    # Create a mock large image file
    img_data = BytesIO(b"fake_large_image_data" * 1000)  # Simulate a large file
    img_data.name = "large_image.jpg"

    # Simulate the file upload to the prediction route
    response = client.post(
        "/prediction",  # The route for prediction
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Assertions: Ensure the response status code is 200 and check for prediction content
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Modify based on your prediction output

def test_acceptance_valid_image_size_upload(client):
    """Test acceptance of a valid image file of a specific size or resolution."""
    img_data = BytesIO(b"valid_image_data_of_large_size" * 1000)  # Simulating a large image file
    img_data.name = "large_image.jpg"

    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Ensure successful upload with a 200 status code
    assert response.status_code == 200
    assert b"Prediction" in response.data  # Ensure the response includes prediction data
