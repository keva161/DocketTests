import pytest
import requests
from config import config
from utils.Generate import Generate

# These fixtures run before the tests and gener the user, and API tokens that are used in the tests.
# The token fixture also deletes the account associated with the generated token once the test has run.

@pytest.fixture
def user():
    generator = Generate()
    user = generator.GetUser()
    yield user

@pytest.fixture()
def token():
    generator = Generate()
    token = generator.GetToken()
    yield token
    requests.delete(config.SERVER + '/api/Users/', headers={'token': token})
