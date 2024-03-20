#!/bin/sh

PYTHON_VERSION=3,12

pipenv --venv
pipenv --rm
pipenv --venv
rm Pipfile*

pipenv install pytest --pre --python ${PYTHON_VERSION}
pipenv install --dev black
