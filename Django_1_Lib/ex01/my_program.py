import sys
sys.path.insert(0, './local_lib')

from path import Path

# Create a folder and a file, write something in it, and display its content
p = Path('my_directory')
p.mkdir_p()
f = p / 'my_file.txt'
f.write_text('Hello, World!')

# Read and display the file content
print(f.text())