try:
    from path import Path
except ImportError:
    print("Module 'path' is not installed")
    Path = None

# Create a folder and a file, write something in it, and display its content
p = Path('my_directory')
p.mkdir_p()
f = p / 'my_file.txt'
f.write_text('Hello, World!')

# Read and display the file content
print(f.read_text())