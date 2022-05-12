import pytest

def test_no_markers():
    assert True

@pytest.mark.sole_marker
def test_sole_marker():
    assert True

@pytest.mark.marker1
@pytest.mark.marker2
def test_two_markers():
    assert True

@pytest.mark.record_prop
def test_record_property(record_property):
    record_property("data", 3)
    assert True
