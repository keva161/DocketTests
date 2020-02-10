from endpoints.Register import Register

def test_register_new_user(user):
    # This test registered a new user.
    Registration = Register()
    result = Registration.CreateUser(user)

    assert "Current user deleted" in result