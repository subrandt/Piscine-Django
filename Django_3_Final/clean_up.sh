#!/bin/bash

# Execute this script with:
# source clean_up.sh

# Deactivate the virtual environment if it's active
if [[ "$VIRTUAL_ENV" != "" ]]; then 
    deactivate
fi

# Remove the virtual environment
rm -rf virtualenv

# Clean message
echo "Virtual environment deactivated and removed"
