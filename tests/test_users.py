import pytest
from endpoints.Users import Users

def test_get_all_users(token):
    users = Users(token)
    result = users.GetAllUsers()
    assert result == 200

def test_delete_users(token):
    users = Users(token)
    result = users.DeleteUser()
    assert "Current user deleted" in result

def test_update_users(user, token):
    users = Users(token)
    result = users.UpdateUser(user)
    assert "Record updated!" in result