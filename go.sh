#!/usr/bin/env bash

git config --global core.autocrlf true
cd /work
export PYTHONPATH=/work
python3 py/all.py

