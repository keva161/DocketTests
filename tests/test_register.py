import pytest
from endpoints.Register import Register

def test_register_new_user(user):
    Registration = Register(user)

    assert "New user created!" in Registration.CreateUser()