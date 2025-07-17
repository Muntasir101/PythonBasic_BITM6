import pytest

@pytest.mark.parametrize("username,password,expected",[
    ("admin", "123456", "Login"),
    ("admin123", "12345623", "Login Error"),
    ("", "", "Login Error")
])

def test_login_data(username,password,expected):
    if username == "admin" and password == "123456" and expected=="Login":
        print("Test Executed for valid")
    else:
        print("Test Executed for invalid")