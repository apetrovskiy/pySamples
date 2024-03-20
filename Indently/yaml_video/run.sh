#!/bin/sh

pipenv run python3 ./main.py
cd translations || exit
pipenv run python3 ./sample_script.py
cd ..
