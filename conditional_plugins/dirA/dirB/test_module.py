import pytest

def test_control():
    assert True

#--------------------------------------------------
# CASE X
def test_fixture_1_x(fixture_1):
    assert fixture_1 == "x1"

def test_fixture_2_x(fixture_2):
    assert fixture_2 == "x2"

#--------------------------------------------------
# CASE Y
def test_fixture_1_y(fixture_1):
    assert fixture_1 == "y1"

def test_fixture_2_y(fixture_2):
    assert fixture_2 == "y2"

#--------------------------------------------------
# CASE YC
def test_fixture_1_yc(fixture_1):
    assert fixture_1 == "y1c"

def test_fixture_2_yc(fixture_2):
    assert fixture_2 == "y2c"
