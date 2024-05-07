#!/bin/bash

# Execute this script with:
# source prepare_hello_world.sh

# Create a virtual environment
python3 -m venv django_venv

# Activate the virtual environment
source django_venv/bin/activate

# Install the dependencies
pip install -r requirement.txt

