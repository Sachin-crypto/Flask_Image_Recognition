

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
