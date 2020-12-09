import pytest

@pytest.fixture(scope='session')
def common_fix():
    return "common_in"

@pytest.fixture(scope='session')
def inner_fix():
    return "inner"
