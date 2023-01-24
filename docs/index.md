
<p align="center">
    <em>Quickly creating a new Modern Python project and publishing it to PyPI ✨</em>
</p>

<p align="center">
<a href="https://github.com/yezz123/pypi-python-template/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/yezz123/pypi-python-template/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/yezz123/pypi-python-template">
    <img src="https://codecov.io/gh/yezz123/pypi-python-template/branch/main/graph/badge.svg"/>
</a>
</p>

## Features

- use `hatch` to manage dependencies.
- use `pre-commit` to manage formatting and linting.
- use `pytest` to run tests.
- use `coverage` to generate coverage reports.
- use `mypy` to check types.
- use `black` to format code.
- use `ruff` to lint code.
- use `isort` to sort imports.
- Set of scripts to run all the commands. e.g. `bash scripts/test.sh` , `bash scripts/test_html.sh` , `bash scripts/format.sh` , `bash scripts/lint.sh` .
- GitHub Actions to run tests, lints and publish to PyPI.
- Use `Dependabot` to keep dependencies up to date.
- Use `MkDocs` to generate documentation.
- Use `Mkdocs-material` for beautiful documentations Theme.

## Installation

You can add pypi-python-template in a few easy steps. First of all, install the dependency:

```shell
$ pip install pypi-python-template

---> 100%

Successfully installed pypi-python-template
```

## Development 🚧

### Setup environment 📦

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
pip install -e .[test,lint,docs]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/test.sh
```

> Note: You can also generate a coverage report with:

```bash
bash scripts/test_html.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

Execute the following command to apply `mypy` type checking:

```bash
bash scripts/lint.sh
```

### Generate documentation 📖

You can start the documentation with:

```bash
bash scripts/docs.sh
```

## [License](license.md)

This project is licensed under the terms of the MIT license.
