#!/bin/sh

PYTHON_VERSIOM=3.12

pipenb --venv
pipenv --rm
pipenv --venv
rm Pipfile*

pipenv install pyyaml --pre --python ${PYTHON_VERSIOM}
pipenv install --dev black --pre
