"""
test_integration_sad.py

Integration tests for sad path scenarios of the Flask image prediction application.
These tests cover:

1. Missing file uploads to the `/prediction` endpoint.
2. Ensuring the application responds gracefully with an error message.
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Fixture for the Flask test client."""
    with app.test_client() as client:
        yield client

def test_missing_file(client):
    """Test the prediction route with a missing file."""
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed." in response.data  # Check if the error message is displayed
