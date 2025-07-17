import pytest

def test_registration_valid(launch_browser):
    print("Account Created.")

@pytest.mark.skip
def test_registration_invalid(launch_browser):
    print("Registration Failed.")