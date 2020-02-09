import pytest
from endpoints.Register import Register

# This test registered a new user, and then deletes the account.


def test_register_new_user(user):
    Registration = Register()
    result = Registration.CreateUser(user)

    assert "Current user deleted" in result