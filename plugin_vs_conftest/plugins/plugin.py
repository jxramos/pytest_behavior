import pytest

@pytest.fixture(scope='session')
def common_fix():
    return "from_plugin"

@pytest.fixture(scope='session')
def plugin_only_fix():
    return "plugin_only"
