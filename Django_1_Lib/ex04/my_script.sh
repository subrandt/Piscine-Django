#!/bin/bash

# Execute this script with:
# Don't do that in shared folder!!!
# source my_script.sh

# Create a virtual environment
python3 -m venv django_venv

# Change permissions
chmod -R 755 lib

# Activate the virtual environment
django_venv/bin/activate

# Install the dependencies
pip install -r requirement.txt
