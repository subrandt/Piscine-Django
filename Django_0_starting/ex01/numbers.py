def display_numbers_from_file():
    try:
        file = open("numbers.txt")
        numbers = file.read()
        print(numbers.replace(",", "\n"))

    except Exception as e:
        print(f"toto {e}")

if __name__ == '__main__':
    display_numbers_from_file()