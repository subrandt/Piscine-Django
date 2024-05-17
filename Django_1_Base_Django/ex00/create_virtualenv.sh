#!/bin/bash

# Execute this script with:
# source create_virtualenv.sh

# Create a virtual environment
python3 -m venv virtualenv

# Activate the virtual environment
source virtualenv/bin/activate

# Install the dependencies
pip install -r requirement.txt