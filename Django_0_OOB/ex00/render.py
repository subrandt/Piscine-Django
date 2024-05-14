import os
import sys
import re
import settings

def generate_CV(template_file: str):

    # read the template file
    with open(template_file, 'r') as file:
        content = file.read()

    # replace placeholders from template_file with values from settings.py
    content = content.format(**vars(settings))

    # create a new file with the same name as the template file but without the .template extension
    with open(template_file.replace('.template', '.html'), 'w') as file:
        file.write(content)

def error_handling_template_file(template_file: str):

    # check extension
    if not template_file.endswith('.template'):
        print("Usage: render.py <templatefile>.template")
        sys.exit(1)
        
    # check if the file exists
    if not os.path.exists(template_file):
        print(f"Error: {template_file} does not exist.")
        sys.exit(1)
    
    # check if it is a file
    if not os.path.isfile(template_file):
        print(f"Error: {template_file} is not a file.")
        sys.exit(1)
    
    # check if the file is empty
    if os.stat(template_file).st_size == 0:
        print(f"Error: {template_file} is empty.")
        sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: render.py <templatefile>.template")
        sys.exit(1)

    error_handling_template_file(sys.argv[1])
    generate_CV(sys.argv[1])