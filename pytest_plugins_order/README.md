# Pytest Plugins Order Experiment
This experiment is meant to illustrate the fixture resolution precedence across `pytest_plugins`
plugin order.

- [Directory Structure](#directory_structure)
- [Overview](#overview)
- [Test Results (Case First)](#test_results_first)
- [Test Results (Case Second)](#test_results_second)
- [Observations](#observations)
    - [Case First](#observations_first)
    - [Case Second](#observations_second)
- [Summary](#summary)

## Directory Structure <a name = "directory_structure"></a>
Several plugin directories and a test module nested in its own subdirectory unrelated to the plugin directory.
```shell
$ tree pytest_plugins_order/
pytest_plugins_order/
├── README.md
├── conftest.py
├── plugins
│   ├── first.py
│   └── second.py
└── test_plugins_order.py
```

## Overview <a name = "overview"></a>

What we find in this experiment is that the fixtures from the latter plugins in the `pytest_plugins`
list take precedence over those that come first in the list. Apparently those plugins are processed
first to last and the definitions from the last override any of those that come before.


## Test Results (Case First) <a name = "test_results_first"></a>

<details>
<summary>Click to expand!</summary>
<pre>
$ pytest --case_var first  pytest_plugins_order --verbose --capture=no
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/USERX/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/USERX/pytest_behavior
plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, cases-2.2.5, remotedata-0.3.1
collected 2 items

pytest_plugins_order/test_plugins_order.py::test_first_order FAILED
pytest_plugins_order/test_plugins_order.py::test_second_order PASSED

======================================================== FAILURES =========================================================
____________________________________________________ test_first_order _____________________________________________________

common_fix = 'second'

    def test_first_order(common_fix):
>       assert common_fix == "first"
E       AssertionError: assert 'second' == 'first'
E         - second
E         + first

pytest_plugins_order/test_plugins_order.py:2: AssertionError
=========================================== 1 failed, 1 passed in 0.06 seconds ============================================
</pre>
</details>
<br>

## Test Results (Case Second) <a name = "test_results_second"></a>

<details>
<summary>Click to expand!</summary>
<pre>
$ pytest --case_var second  pytest_plugins_order --verbose --capture=no
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/USERX/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/USERX/pytest_behavior
plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, cases-2.2.5, remotedata-0.3.1
collected 2 items

pytest_plugins_order/test_plugins_order.py::test_first_order PASSED
pytest_plugins_order/test_plugins_order.py::test_second_order FAILED

======================================================== FAILURES =========================================================
____________________________________________________ test_second_order ____________________________________________________

common_fix = 'first'

    def test_second_order(common_fix):
>       assert common_fix == "second"
E       AssertionError: assert 'first' == 'second'
E         - first
E         + second

pytest_plugins_order/test_plugins_order.py:6: AssertionError
=========================================== 1 failed, 1 passed in 0.06 seconds ============================================
</pre>
</details>
<br>

# Observations <a name = "observations"></a>

## Case First <a name = "observations_first"></a>
In the first case we find that the second test case passes, that is because the second fixture is
loaded last and overrides the fixture seen earlier in the first plugin.

```shell
$ pytest --case_var first  pytest_plugins_order --verbose --capture=no | grep test_
pytest_plugins_order/test_plugins_order.py::test_first_order FAILED
pytest_plugins_order/test_plugins_order.py::test_second_order PASSED
```

<br>

## Case Second <a name = "observations_second"></a>
In the second case we find that the first test case passes, that is because the first fixture is
loaded last and overrides the fixture seen earlier in the second plugin.

```shell
$ pytest --case_var second  pytest_plugins_order --verbose --capture=no | grep test_
pytest_plugins_order/test_plugins_order.py::test_first_order PASSED
pytest_plugins_order/test_plugins_order.py::test_second_order FAILED
```

<br>


# Summary <a name = "summary"></a>
The net result from this experiment isn't too surprising, pytest takes the precedence of the fixture
that shows up last in the pytest_plugins plugins. This makes sense from a loading of fixtures being
done iteratively, the fixtures from the first plugin loaded, the the fixtures from the second plugin,
and so on. So the fixtures of the last plugin in the list will override any that came before.
