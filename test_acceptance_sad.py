"""
test_acceptance_sad.py

This module contains acceptance tests for sad path scenarios of the
Flask image prediction application, integrated with a mock Keras model
to simulate automated system behavior.

The tests cover:

1. Uploading requests with missing files
2. Handling invalid or incorrect input data

Each test ensures the application gracefully handles errors and returns
appropriate responses, while isolating external dependencies via mocks.
"""

import pytest
from unittest.mock import patch, MagicMock


@pytest.fixture
def _client():
    """
    Fixture for the Flask test client with mocked Keras model.
    - Purpose: Set up a test client for making requests to the Flask app during testing.
    - Integration: Mocks the Keras model to isolate the test from the actual ML model,
      enabling automated system integration testing without requiring the real model.
    - Usage: Provides a `_client` object to use for HTTP request simulations.
    """
    from unittest.mock import patch, MagicMock
    import app  

    with patch("model.load_model") as mock_load_model:
        mock_model = MagicMock()
        mock_model.predict.return_value = [[0.1, 0.9]]
        mock_load_model.return_value = mock_model

        with app.app.test_client() as client:
            yield client

def test_acceptance_missing_file(_client):
    """
    Test Case: No File Uploaded
    - Purpose: Validate the application's behavior when no file is provided in the upload request.
    - Scenario:
        - Simulate a POST request to the `/prediction` route with no file data.
        - Assert the response status code is 200 (to indicate a valid request was processed).
        - Verify that the response includes an appropriate error message.
    - Integration: Uses the mocked Keras model to ensure the test focuses on request handling
      and error response without dependency on the actual model.
    """
    response = _client.post("/prediction", data={}, content_type="multipart/form-data")


    assert response.status_code == 200
    assert b"File cannot be processed" in response.data