# PBL 8: Unit testing

This session is an opportunity to practice creating and running a test case using the Paralympics web app scenario.
There is also an opportunity to see the information that results from using GitHub Actions for continuous integration (
automatically running tests when code is committed/pushed to GitHub) and linting (automatically checking for code
quality).

The activities use pytest as the test library, pytest-cov for coverage and flake8 for linting.

- [Problem 1: Test files and folders](#problem-1-test-files-and-folders)
- [Problem 2: Create a fixture](#problem-2-create-a-fixture)
- [Problem 3: Create and run a unit test](#problem-3-create-and-run-a-unit-test)
- [Problem 4: Run a coverage report](#problem-4-run-a-coverage-report)
- [Problem 5: Create an additional test](#problem-5-create-an-additional-test)
- [Problem 6: Setup GitHub Actions to run the tests](#problem-6-setup-github-actions-to-run-the-tests)

## Set up

1. Create a new repository from the template
   repository [https://github.com/ucl-comp0035/comp0035-pbl8](https://github.com/ucl-comp0035/comp0035-pbl8).
2. Clone the repository in your IDE (VS Code, PyCharm etc.).
3. Create and activate a venv. In VS Code you can use the command pallet and find the option 'Python: Create
   Environment'.
4. Install pytest and pytest-cov e.g., `pip install pytest pytest-cov`.

## Problem 1: Test files and folders

The sample repo has a models.py file that has the classes from the UML class diagram. Some methods have been
implemented.

Please note that the code is rudimentary and is not an example of how the methods will actually be written when we use
Flask and Dash in term 2.

There are some deliberate errors in the code, and no doubt some un-intentional errors too!

**Remember to
use [appropriate naming conventions](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#choosing-a-test-layout-import-rules)
.**

1. Create a directory for the tests.
2. In the directory, create an empty Python file in which you will write tests for the classes in `models.py`.
3. In the directory, create a new Python file called `conftest.py`. `conftest.py'` provides a location for fixtures and
   configuration for pytest.

## Problem 2: Create a fixture

[Fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) can be used to provide static data and helper functions for
your tests. Fixtures don't have to be placed in `conftest.py` however by placing them here, all your tests could access
the fixtures contained.

1. In `conftest.py`, add a fixture that provides data to create a new `general public` user.

Hints:

The following example shows the structure of a fixture:

```python
import pytest


@pytest.fixture(scope='module')
def values():
    values = [2, 4, 8, 20]
    yield values
```

Decide on the [scope](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#fixture-scopes).

Use a meaningful function name to describe what the fixture provides. You are creating a fixture that provides data to
create a new `general public` user

To create a new user import the GeneralPublic class from para_cycle.models and create an instance of the class with
values for each of the attributes (username, password, email, phone).

The following code shows an example of how to use the `GeneralPublic` class in `models.py` to create a new user.

```python
from para_cycle.models import GeneralPublic

gp_user = GeneralPublic(username='uname', password='pass', email='email@email.com', phone='09999 999999')
```

## Problem 3: Create and run a unit test

1. Write Python code in the python test file you created in Problem 1 to create the following test. It should use the
   fixture that you created in Problem 2.

The test has been described using the Given-When-Then model:

```text
GIVEN a new user (created as a fixture)
WHEN the user has just been created
THEN the logged in status should be False
```

Tests can be written as functions within your test python file; or you can create test classes.

Example of a **test function** that uses a fixture called 'values':

```python
def test_minimum_returns_correct_value(values):
    """
    GIVEN the values 2, 4, 8 and 20
    WHEN the values are passed to the minimum function 
    THEN the result should equal 2
    """
    result = algorithm.minimum(values)
    assert result == 2
```

Example of a **test class** that uses a fixture called 'calc' which has a scope of class:

```python
import pytest

from calculator.calculator_class import Calculator


@pytest.mark.usefixtures("calc")
class TestCalculator:

    def test_add(self):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the add function is called
        THEN the result is 12
        """
        result = calc.add()
        assert result == 12

    def test_subtract(self):
        """
        GIVEN a Calculator with the values 9 and 3
        WHEN the subtract function is called
        THEN the result is 6
        """
        result = calc.subtract()
        assert result == 6
```

Decide on a test function (or a test class with a method/function in the class), and write the test name (remember to
use a meaningful test name).

Write the test using the GIVEN-WHEN-THEN model to guide you:

- GIVEN a new user (created as a fixture): pass the fixture as a parameter to the test function (or class)
- WHEN the user has just been created: in this case you don't need to do anything further, the fixture should provide a
  new user
- THEN the logged in status should be False: use
  an [assertion](https://docs.pytest.org/en/7.1.x/how-to/assert.html#how-to-write-and-report-assertions-in-tests) to
  test that the `_is_logged_in` parameter of the GeneralUser object is FALSE. There is a good list of
  different [assert uses with examples here](https://understandingdata.com/list-of-python-assert-statements-for-unit-tests/)
  .


2. Run the test code with pytest using the verbose parameter. Either use your IDE's interface or the command line.

Refer to
the [Pytest guide on how to invoke pytest](https://docs.pytest.org/en/7.1.x/how-to/usage.html#how-to-invoke-pytest).

To run Pytest from the terminal command prompt:

```
python -m pytest -v
```

You will need to read how to configure your IDE to use Pytest. Once you have configured it, then you should have a run
test function in your IDE.

- [VS Code pytest](https://code.visualstudio.com/docs/python/testing#_configure-tests). Use the science flask symbol in
  the left bar, click on it, then select 'Configure Python tests', select pytest from the options, then select the name
  of the test directory you created in problem 1 (likely to be test or tests).
- [PyCharm pytest](https://www.jetbrains.com/help/pycharm/pytest.html)

Did the tests run OK or fail with an error message indicating it could not find the package or module para_cycle?

Read
the [pytest good integration practices](https://docs.pytest.org/en/6.2.x/goodpractices.html#install-package-with-pip)
which explains how and why to install your code as a package before testing. The steps it tells you are:

1. Create a `setup.py` file in the root folder of the project directory, e.g.

```python
from setuptools import setup, find_packages

setup(
    name="pbl8",
    packages=find_packages()
)
```

2. You can then install your package in "editable" mode by running from the same directory:

`pip install -e .`

which lets you change your source code (both tests and application) and rerun tests at will.

There is more detail on the [use of `setup.py` here](https://docs.python.org/3.10/distutils/setupscript.html).

You may also need to repeat the steps to configure Pytest in VS Code to find the tests.

## Problem 4: Run a coverage report

1. Run the tests using coverage with the optional parameters and identify which lines are not covered by tests.

The general syntax to run pytest with coverage from the terminal is as follows, where 'package_name' is the package you
wish to check coverage for:

```
python -m pytest --cov=package_name
```

The general syntax to run pytest from the terminal with coverage and a more detailed report showing lines not covered by
tests is shown as follows:

```
python -m pytest --cov-report term-missing --cov=package_name tests/
```

Run pytest with coverage for the `para_cycle` package.


<hr>

> There is one solution to problems 1-4 in [https://github.com/shiressl1/pbl8-soln](https://github.com/shiressl1/pbl8-soln)

<hr>

## Problem 5: Create an additional test

1. Create another test using the Given-When-Then model:

```text
GIVEN a user is logged in
WHEN the logout function is called
THEN the logged in status should be False
```

2. Run the test with coverage.

Extensions:

Refer to the [pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/readme.html).

- consider the lines of code not currently covered, write another test that improves your coverage.
- run coverage and [report the results to html](https://pytest-cov.readthedocs.io/en/latest/reporting.html). After
  running open index.html in the cov_html directory. Click on the files names to see the missing lines.

## Problem 6: Setup GitHub Actions to run the tests

GitHub Actions provides a way to automatically run a defined series of steps (called a 'workflow') that happens on a
given change to your repository.

In this repo a GitHub Actions workflow has already been created that runs the tests and a linter whenever code is
updated in the main/master branch. You can see the structure of the workflow in `.github/workflows/python-app.yml`.

Creating a workflow is covered in the [teaching materials](https://nicholsons.github.io/comp0034-5/how-to/ht-ci.html)
and on
GitHub, [see this guide to testing Python apps on GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
.

The purpose of this 'problem' is to use the information available in the workflow reports on GitHub to decide what
changes you may need to make to your code.

1. Commit and push your changes to GitHub.
2. Go to the repository on GitHub and find the Actions tab.
3. Under 'All workflows' select the 'Python application' workflow.
4. Click on the most recent workflow run.
5. Click on 'build'.
6. Expand the section for 'Lint with flake8' and 'Test with pytest and cov' (click on the '>' symbol to expand).
    - What does the information tell you?
    - What actions could you take as a result of this information?

## Problem 7: Challenge yourself

Challenge yourself to explore other features of Pytest, e.g. run the tests with multiple different general user
objects (hint: look up pytest parameterised tests on [Pytest](https://docs.pytest.org/en/7.1.x/how-to/parametrize.html),
or search for tutorials on the topic).

Explore the use of mocks with pytest,
for [example here](https://levelup.gitconnected.com/a-comprehensive-guide-to-pytest-3676f05df5a0).
