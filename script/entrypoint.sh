#!/bin/sh
set -e
flask db upgrade
python run.py