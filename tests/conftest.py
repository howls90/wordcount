import pytest
from app import app as server
from database import DB
from app import setUpLogs, setUpDb

@pytest.fixture
def app():
    app = server
    setUpLogs()
    setUpDb('config.TestingConfig')
    return app
