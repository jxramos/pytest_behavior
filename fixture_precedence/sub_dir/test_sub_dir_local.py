import pytest

@pytest.fixture
def common_fix():
    return "common_local"

def test_common_fix_local(common_fix):
    assert common_fix == "common_in"
