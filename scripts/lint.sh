#!/usr/bin/env bash

set -e
set -x

mypy --show-error-codes pypi_python_template tests
