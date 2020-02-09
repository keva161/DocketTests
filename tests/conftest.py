import pytest
import requests
from utils.Generate import Generate

@pytest.fixture
def user():
    generator = Generate()
    user = generator.user()
    yield user

@pytest.fixture()
def token():
    generator = Generate()
    token = generator.token()
    yield token
    requests.delete('http://127.0.0.1:5000/api/Users/', headers={'token': token})
