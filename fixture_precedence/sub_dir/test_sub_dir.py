def test_true():
    assert True # control test

def test_common_fix(common_fix):
    assert common_fix == "common_in"

def test_inner_fix(inner_fix):
    assert inner_fix == "inner"

def test_outer_fix(outer_fix):
    assert outer_fix == "outer"
