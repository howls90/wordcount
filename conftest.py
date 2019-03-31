import pytest
from app import app as server

# Creates a fixture whose name is "app"
# and returns our flask server instance
@pytest.fixture
def app():
    app = server
    return app
