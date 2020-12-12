import argparse
import os
import sys
import pytest


CASE_VAR = "case_var"
CASE_VAR_ARG = "--" + CASE_VAR
case_var_default = "second"
case_var = case_var_default
if CASE_VAR_ARG in sys.argv:
    idx = sys.argv.index(CASE_VAR_ARG) + 1
    case_var = sys.argv[idx]

parser = argparse.ArgumentParser()
parser.add_argument(
    CASE_VAR_ARG,
    choices=["first", "second"],
    default=case_var_default,
    help="The pytest plugin selection",
)
args = parser.parse_args([CASE_VAR_ARG, case_var])


# Condition the pytest plugins on the case variable
if args.case_var == "first":
    pytest_plugins = ["plugins.first", "plugins.second"]
else:
    pytest_plugins = ["plugins.second", "plugins.first"]

# Make the pytest understand the command line argument
def pytest_addoption(parser):
    parser.addoption(
        CASE_VAR_ARG,
        default=case_var_default,
        help="The experiment case to be evaluated against.",
    )
