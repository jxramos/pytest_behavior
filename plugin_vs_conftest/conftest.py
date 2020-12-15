import pytest

pytest_plugins = ["plugins.plugin"]

@pytest.fixture(scope='session')
def common_fix():
    return "from_conftest"
