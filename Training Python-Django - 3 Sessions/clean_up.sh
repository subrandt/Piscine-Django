#!/bin/bash

# Execute this script with:
# source clean_up.sh

# Deactivate the virtual environment if it's active
if [[ "$VIRTUAL_ENV" != "" ]]; then 
    deactivate
fi

# Remove the virtual environment
rm -rf virtualenv

# Empty the logs.txt file
rm -f d04/logs/logs.txt

# Clean message
echo "Virtual environment deactivated and removed"