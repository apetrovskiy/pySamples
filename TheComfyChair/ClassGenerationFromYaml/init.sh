#!/bin/sh

PYTHON_VER=3.12

pipenv --venv
pipenv --rm
pipenv --venv
rm Pipfile*

pipenv install pyyaml beartype python-dotenv --pre --python ${PYTHON_VER}
pipenv install --dev black --pre
