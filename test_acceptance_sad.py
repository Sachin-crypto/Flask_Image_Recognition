
import pytest
from app import app


@pytest.fixture
def client():
    """
    Fixture for the Flask test client.
    Provides a client for sending HTTP requests to the Flask application.
    """
    with app.test_client() as client:
        yield client


def test_acceptance_missing_file(client):
    """
    Test Case: No File Uploaded

    Verify that the application handles a request without an uploaded file
    and displays an appropriate error message.
    """
    # Send a POST request without any uploaded file.
    response = client.post(
        "/prediction",
        data={},
        content_type="multipart/form-data"
    )

    # Verify that the request is handled successfully.
    assert response.status_code == 200

    # Verify that the appropriate error message is displayed.
    assert b"Please select an image file." in response.data
