"""
Conftest configuration for pytest fixtures.
"""

import pytest
from app import app  # Import Flask app

@pytest.fixture
def client():
    """Provide a test client for Flask app."""
    with app.test_client() as client:
        yield client
