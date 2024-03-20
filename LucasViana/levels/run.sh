#!/bin/sh

pipenv run black .
pipenv run python3 main.py
