# pytest_behavior
A simple set of folders with test cases and pytest infrastructure to demonstrate different aspects of pytest behavior.


# Fixture Precedence
This experiment demonstrates how a fixture whose name is reused across a conftest.py hierarchy takes precedence
with respect to a test module. The net result: fixtures are resolved closest to the test module itself
when using `conftest.py` files alone for fixture definitions.
