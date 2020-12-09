import pytest

@pytest.fixture(scope='session')
def common_fix():
    return "common_out"

@pytest.fixture(scope='session')
def outer_fix():
    return "outer"
