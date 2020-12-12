"""
The root conftest.py file for this project
"""

import argparse
import os
import sys
import pytest


# Narrowed command line argument parsing
#   this is necessary to interoperate with pytest command line arguments while also validating the
#   input to a fixed set of choices.
CASE_VAR = "case_var"
CASE_VAR_ARG = "--"+CASE_VAR
case_var_default = "yc"
case_var = case_var_default
if CASE_VAR_ARG in sys.argv:
    idx = sys.argv.index(CASE_VAR_ARG) + 1
    case_var = sys.argv[idx]
elif CASE_VAR in os.environ:
    case_var = os.environ[CASE_VAR]

parser = argparse.ArgumentParser()
parser.add_argument(CASE_VAR_ARG, choices=["x", "y", "yc"], default=case_var_default, help="The pytest plugin selection")
args = parser.parse_args([CASE_VAR_ARG, case_var])


# Condition the pytest plugins on the case variable
if args.case_var == "x":
    pytest_plugins = [
        "pluginsX.plugin_x"
    ]
elif args.case_var == "y":
    pytest_plugins = [
        "pluginsY.plugin_y"
    ]
else:
    pytest_plugins = [
        "pluginsY.pluginsYc.plugin_yc"
    ]

# Make the pytest understand the command line argument
def pytest_addoption(parser):
    parser.addoption(
        CASE_VAR_ARG,
        default=case_var_default,
        help="The experiment case to be evaluated against.",
    )

## ERRONEOUS fixture attempt
#@pytest.fixture(scope="session", autouse=True)
#def plugin_case(pytestconfig):
#    """
#    This fixture does not in fact work as expected, you actually yield the following error
#    E               NameError: name 'pytest_plugins' is not defined
#    Even the presence of the global reference is still not enough.
#    """
#    #global pytest_plugins
#
#    case_var = pytestconfig.getoption("--case_var")
#    if "x" in case_var:
#        pytest_plugins[:] = [
#            "pluginsX.plugin_x"
#        ]
#    elif "y" in case_var:
#        pytest_plugins[:] = [
#            "pluginsY.plugin_y"
#        ]
#    else:
#        pytest_plugins[:] = [
#            "pluginsY.pluginsYc.plugin_yc"
#        ]
#    print(f"case_var={case_var}")
#
