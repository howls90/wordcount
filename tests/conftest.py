import pytest
from app import app as server

@pytest.fixture
def app():
    app = server
    return app
