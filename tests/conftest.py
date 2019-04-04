import pytest
from database import DB
from app import setUpDb
from app import app as server


@pytest.fixture
def app():
    app = server
    setUpDb(app, 'config.TestingConfig')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
