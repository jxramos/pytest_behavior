import pytest

def test_control():
    assert True

def test_plugin(common_fix):
    assert common_fix == "from_plugin"

def test_conftest(common_fix):
    assert common_fix == "from_conftest"

def test_plugin_only_fixture(plugin_only_fix):
    assert plugin_only_fix == "plugin_only"
