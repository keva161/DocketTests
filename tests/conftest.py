import pytest
from utils.Generate import Generate

@pytest.fixture
def user():
    user = Generate()
    return user
