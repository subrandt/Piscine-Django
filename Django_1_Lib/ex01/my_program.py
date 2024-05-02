try:
    from path import Path
except ImportError:
    print("Module 'path' is not installed")
    Path = None

if Path is not None:
    # Create a folder and a file, write something in it, and display its content
    folder = Path('my_directory')
    folder.mkdir_p()
    assert folder.exists(), "Failed to create directory"


    filename = folder / 'my_file.txt'
    filename.write_text('Hello, World!')
    assert filename.exists(), "Failed to create file"


    # Read and display the file content
    print(filename.read_text())
else:
    print("Cannot execute the program because 'path' module is not installed")