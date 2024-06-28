#!/bin/bash

# Execute this script with:
# source create_virtualenv.sh

# Delete the virtual environment if it exists
if [ -d "myenv" ]; then
    rm -rf myenv
fi

# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the dependencies
pip install -r requirements.txt

