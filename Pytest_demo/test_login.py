import pytest

@pytest.mark.smoke
def test_case1_valid(launch_browser):
    print("Test Case 1 - Valid Executed.")

@pytest.mark.skip
@pytest.mark.smoke
def test_case2_valid(launch_browser):
    print("Test Case 2 - Valid Executed.")

@pytest.mark.regression
def test_case3_invalid(launch_browser):
    print("Test Case 3 - inValid Executed.")

@pytest.mark.regression
def test_case4_invalid(launch_browser):
    print("Test Case 4 - inValid Executed.")