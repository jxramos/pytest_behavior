# Conditional Plugins Experiment
This experiment is meant to illustrate the import behavior across a simple sample project to show the conditional
import behavior that is possible with different plugins based on an environment variable or command line argument's
value. This is one possible avenue for reusing a test module for different implementations of an API.

- [Directory Structure](#directory_structure)
- [Overview](#overview)
- [Test Results (Environment Variable--Case x)](#test_results_x)
- [Test Results (Environment Variable--Case y)](#test_results_y)
- [Test Results (Environment Variable--Case yc)](#test_results_yc)
- [Observations](#observations)
    - [Case X](#observations_x)
    - [Case Y](#observations_y)
    - [Case Yc](#observations_yc)
    - [Command Line Argument](#observations_command_line)
- [Summary](#summary)
- [Relevant Documentation](#documentation)

## Directory Structure <a name = "directory_structure"></a>
Several plugin directories and a test module nested in its own subdirectory unrelated to the plugin directory.
```shell
conditional_plugins/
├── README.md
├── conftest.py
├── dirA
│   └── dirB
│       ├── conftest.py
│       └── test_module.py
├── pluginsX
│   └── plugin_x.py
└── pluginsY
    ├── plugin_y.py
    └── pluginsYc
        └── plugin_yc.py
```

## Overview <a name = "overview"></a>

What we find in this experiment is that we can in fact conditionally load different fixture implementations as seen by the
moving set of failures and passing test cases meant to illustrate the fixture's resolution based on the environment variable.


## Test Results (Environment Variable--Case x) <a name = "test_results_x"></a>

<details>
<summary>Click to expand!</summary>
<pre>
$ export case_var=x; pytest conditional_plugins/  --verbose  --capture=no
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/USERX/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/USERX/pytest_behavior
plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, cases-2.2.5, remotedata-0.3.1
collected 7 items

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED

======================================================== FAILURES =========================================================
____________________________________________________ test_fixture_1_y _____________________________________________________

fixture_1 = 'x1'

>   ???
E   AssertionError: assert 'x1' == 'y1'
E     - x1
E     + y1

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:17: AssertionError
____________________________________________________ test_fixture_2_y _____________________________________________________

fixture_2 = 'x2'

>   ???
E   AssertionError: assert 'x2' == 'y2'
E     - x2
E     + y2

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:20: AssertionError
____________________________________________________ test_fixture_1_yc ____________________________________________________

fixture_1 = 'x1'

>   ???
E   AssertionError: assert 'x1' == 'y1c'
E     - x1
E     + y1c

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:25: AssertionError
____________________________________________________ test_fixture_2_yc ____________________________________________________

fixture_2 = 'x2'

>   ???
E   AssertionError: assert 'x2' == 'y2c'
E     - x2
E     + y2c

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:28: AssertionError
=========================================== 4 failed, 3 passed in 0.08 seconds ============================================
</pre>
</details>
<br>

## Test Results (Environment Variable--Case y) <a name = "test_results_y"></a>

<details>
<summary>Click to expand!</summary>
<pre>
$ export case_var=y; pytest conditional_plugins/  --verbose  --capture=no
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/USERX/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/USERX/pytest_behavior
plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, cases-2.2.5, remotedata-0.3.1
collected 7 items

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED

======================================================== FAILURES =========================================================
____________________________________________________ test_fixture_1_x _____________________________________________________

fixture_1 = 'y1'

>   ???
E   AssertionError: assert 'y1' == 'x1'
E     - y1
E     + x1

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:9: AssertionError
____________________________________________________ test_fixture_2_x _____________________________________________________

fixture_2 = 'y2'

>   ???
E   AssertionError: assert 'y2' == 'x2'
E     - y2
E     + x2

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:12: AssertionError
____________________________________________________ test_fixture_1_yc ____________________________________________________

fixture_1 = 'y1'

>   ???
E   AssertionError: assert 'y1' == 'y1c'
E     - y1
E     + y1c
E     ?   +

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:25: AssertionError
____________________________________________________ test_fixture_2_yc ____________________________________________________

fixture_2 = 'y2'

>   ???
E   AssertionError: assert 'y2' == 'y2c'
E     - y2
E     + y2c
E     ?   +

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:28: AssertionError
=========================================== 4 failed, 3 passed in 0.08 seconds ============================================
</pre>
</details>
<br>

## Test Results (Environment Variable--Case yc) <a name = "test_results_yc"></a>

<details>
<summary>Click to expand!</summary>
<pre>
$ unset case_var; pytest conditional_plugins/  --verbose  --capture=no
=================================================== test session starts ===================================================
platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/USERX/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/USERX/pytest_behavior
plugins: openfiles-0.3.2, arraydiff-0.3, doctestplus-0.3.0, cases-2.2.5, remotedata-0.3.1
collected 7 items

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc PASSED

======================================================== FAILURES =========================================================
____________________________________________________ test_fixture_1_x _____________________________________________________

fixture_1 = 'y1c'

>   ???
E   AssertionError: assert 'y1c' == 'x1'
E     - y1c
E     + x1

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:9: AssertionError
____________________________________________________ test_fixture_2_x _____________________________________________________

fixture_2 = 'y2c'

>   ???
E   AssertionError: assert 'y2c' == 'x2'
E     - y2c
E     + x2

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:12: AssertionError
____________________________________________________ test_fixture_1_y _____________________________________________________

fixture_1 = 'y1c'

>   ???
E   AssertionError: assert 'y1c' == 'y1'
E     - y1c
E     ?   -
E     + y1

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:17: AssertionError
____________________________________________________ test_fixture_2_y _____________________________________________________

fixture_2 = 'y2c'

>   ???
E   AssertionError: assert 'y2c' == 'y2'
E     - y2c
E     ?   -
E     + y2

/Users/USERX/pytest_behavior/conditional_plugins/command_line_args/dirA/dirB/test_module.py:20: AssertionError
=========================================== 4 failed, 3 passed in 0.07 seconds ============================================
</pre>
</details>
<br>

# Observations <a name = "observations"></a>

## Case X <a name = "observations_x"></a>
When we set the environment variable to x we find the x cases pass as expected with all others failing.
```shell
$ export case_var=x; pytest conditional_plugins/  --verbose  --capture=no

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED
```

<br>

## Case Y <a name = "observations_y"></a>
When we set the environment variable to y we find the y cases pass as expected with all others failing.
```shell
$ export case_var=y; pytest conditional_plugins/  --verbose  --capture=no

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED
```

<br>

## Case Yc <a name = "observations_yc"></a>
When we set no environment variable find the yc cases pass as expected with all others failing.
```shell
$ unset case_var; pytest conditional_plugins/  --verbose  --capture=no

conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc PASSED
```

## Command Line Argument <a name = "observations_command_line"></a>
The same set of passing and failing tests manifest when we utilize the command line argument approach as well...

```shell
$ pytest conditional_plugins/  --case_var x --verbose  --capture=no | grep ::test_
conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED

$ pytest conditional_plugins/  --case_var y --verbose  --capture=no | grep ::test_
conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc FAILED

$ pytest conditional_plugins/  --case_var yc --verbose  --capture=no | grep ::test_
conditional_plugins/dirA/dirB/test_module.py::test_control PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_x FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_y FAILED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_1_yc PASSED
conditional_plugins/dirA/dirB/test_module.py::test_fixture_2_yc PASSED
```

# Summary <a name = "summary"></a>
A test module can be reused as is with a common fixture name holding different implementations
defined in distinct plugin files. Since plugin discovery is governed in part by the `pytest_plugins`
global that list must be defined in a global context. Therefore we need a handle on its conditional
values through a mechanism that transcends pytest itself and operates at global scope. The OS environment
variable as well as the command line argument mechanisms are suitable to this end.

An attempt to define the `pytest_plugins` value within a fixture itself seemed unattainable as you
can see if you inspect the section `#ERRONEOUS fixture attempt` in the conftest file.


# Relevant Documentation <a name = "documentation"></a>
- [pytest API Reference](https://docs.pytest.org/en/stable/reference.html?highlight=pytest_plugins#globalvar-pytest_plugins)
- [Requiring/Loading plugins in a test module or conftest file](https://docs.pytest.org/en/stable/writing_plugins.html?highlight=pytest_plugins#requiring-loading-plugins-in-a-test-module-or-conftest-file)
- [Using fixtures from other projects](https://docs.pytest.org/en/stable/fixture.html?highlight=pytest_plugins#using-fixtures-from-other-projects)

> The standard/recommended layout is to have your config file at the root of the tests directory, and
> then `conftest.py´ files placed inside this hierarchy **according to their visibility**.
That is to say according to the visibility you want for them to have, that is what is to override
and ultimately made visible to what test modules.
https://github.com/pytest-dev/pytest/issues/5822#issuecomment-566552697


