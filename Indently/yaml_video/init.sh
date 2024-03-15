#!/bin/sh

pipenv --venv
pipenv --rm
pipenv --venv
rm Pipfile*

pipenv install pyyaml loguru --python 3.12
pipenv install --dev black
