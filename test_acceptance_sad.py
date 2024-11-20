import pytest
from app import app

@pytest.fixture
def client():
    """Fixture for the Flask test client."""
    with app.test_client() as client:
        yield client

def test_acceptance_missing_file(client):
    """Test the scenario where no file is uploaded and ensure the status code is 200 with an appropriate error message."""
    # Simulate a POST request with no file uploaded
    response = client.post("/prediction", data={}, content_type="multipart/form-data")
    
    # Assertions:
    # 1. Ensure the response status code is 200.
    # 2. Ensure that the response contains an appropriate error message, such as "File cannot be processed" or "No file uploaded."
    assert response.status_code == 200
    assert b"File cannot be processed" in response.data  # Or any other error message your app uses
