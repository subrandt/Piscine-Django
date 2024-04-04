def display_numbers_from_file():
    try:
        file = open("number.txt")
        numbers = file.read()
        print(numbers)

    except Exception as e:
        print(f"toto {e}")



if __name__ == '__main__':
    display_numbers_from_file()