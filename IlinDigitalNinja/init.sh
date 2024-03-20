#!/bin/sh

PYTHON_VERSION=3.12

pipenv --venv
pipenv --rm
pipenv --venv
rm Pipfile*

pipenv install --dev black --pre --python $PYTHON_VERSION
