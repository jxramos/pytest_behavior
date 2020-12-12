import pytest


@pytest.fixture(scope="session")
def common_fix():
    return "first"
