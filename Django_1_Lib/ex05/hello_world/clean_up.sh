#!/bin/bash

# Execute this script with:
# source clean_up.sh

# Deactivate the virtual environment if it's active
deactivate 2>/dev/null || true

# Remove the virtual environment
rm -rf django_venv

# Clean message
echo "Virtual environment deactivated and removed"