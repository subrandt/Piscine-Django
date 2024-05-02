#!/bin/bash

# Print the version of pip
pip --version

# Install the development version of path.py
pip install -t ./local_lib --upgrade --force-reinstall git+https://github.com/jaraco/path.py.git > install.log

# Add the local_lib directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)/local_lib"

echo $PYTHONPATH

# run my_program.py
python3 my_program.py