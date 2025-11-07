"""Acceptance tests for happy path image prediction."""

from io import BytesIO


def test_successful_prediction(client):
    """Test successful image upload and prediction."""
    # Create a mock image file with minimal valid content
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

    # Simulate a file upload to the prediction endpoint
    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    # Assertions
    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_png_upload(client):
    """Test uploading PNG image and getting prediction."""
    img_data = BytesIO(b"fake_img_data")
    img_data.name = "test.png"

    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data


def test_upload_large_image(client):
    """Test uploading a large image (~2MB) and getting prediction."""
    img_data = BytesIO(b"a" * 2_000_000)  # 2MB fake image
    img_data.name = "large_test.jpg"

    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data
