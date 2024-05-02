#!/bin/bash

# Afficher la version de pip
pip --version

# Installer la version de développement de path.py
pip install -t ./local_lib --upgrade --force-reinstall git+https://github.com/jaraco/path.py.git > install.log

# execute my_program.py
python3 my_program.py