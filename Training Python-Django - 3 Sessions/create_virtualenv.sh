#!/bin/bash

# Execute this script with:
# source create_virtualenv.sh

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the dependencies
pip install -r requirements.txt

