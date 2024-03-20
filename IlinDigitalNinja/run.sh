#!/bin/sh

pipenv run black .
pipenv run python3 ./file_001_input_output.py
pipenv run python3 ./file_002_variables.py
