from endpoints.Users import Users

def test_get_all_users(token):
    # This test requests all users from the server.
    users = Users(token)
    result = users.GetAllUsers()
    assert "There are no registered users to deliver" not in result

def test_delete_users(token):
    # This test deletes a user.
    users = Users(token)
    result = users.DeleteUser()
    assert "Current user deleted" in result

def test_update_users(user, token):
    # This test updates a users details.
    users = Users(token)
    result = users.UpdateUser(user)
    assert "Record updated!" in result