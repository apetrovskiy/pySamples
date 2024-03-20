#!/bin/sh

pipenv run black .
pipenv run pytest .
