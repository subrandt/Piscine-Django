#!/bin/bash

# Remove existing virtual environment if it exists
if [ -d "myenv" ]; then
	echo "Removing existing virtual environment..."
	rm -rf myenv
fi

# Create a new virtual environment
echo "Creating virtual environment..."
python3 -m venv myenv

# Activate the virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Virtual environment setup complete."