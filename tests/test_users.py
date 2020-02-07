import pytest
from endpoints.Users import Users

def test_get_all_users(user):
    users = Users(user)
    result = users.GetAllUsers()
    assert result == 200

def test_delete_all_users(user):
    users = Users(user)
    result = users.DeleteUsers()
    assert "Current user deleted" in result