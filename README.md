# pytest_behavior
A simple set of folders with test cases and pytest infrastructure to demonstrate different aspects of pytest behavior.


# Fixture Precedence
This experiment demonstrates how a fixture whose name is reused across a conftest.py hierarchy takes precedence
with respect to a test module. The net result: fixtures are resolved closest to the test module itself
when using `conftest.py` files alone for fixture definitions.

# Conditional Plugins
This experiment is meant to illustrate how different fixture implementations can be drawn into a test
module from different plugin folders.

Two techniques are illustrated for the division into cases for how the value of the `pytest_plugins`
gets specified: environment variables and command line arguments. Both must operate at globals scope
since the `pytest_plugins` list must be specified globally at the root folder's conftest file.

# Pytest Plugins Order
This experiment is meant to illustrate the fixture precedence when two fixtures are shared in two referenced
pytest plugins when the order if swapped in the `pytest_plugins` list.
