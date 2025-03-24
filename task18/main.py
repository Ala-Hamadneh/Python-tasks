def main():
    is_running = True
    file = open('names.txt', 'a+')

    while is_running:
        print("\n" + "*" * 35)
        print("File Append Program")
        print("*" * 35)
        print("1 - Append a new name to 'names.txt'")
        print("2 - Close the file and exit")
        print("*" * 35)

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                file.seek(0, 2)
                name = input("Enter a name to add: ")
                file.write("\n" + name)
                print(f"'{name}' was added to the file.")
            case '2':
                is_running = False
                file.close()
            case _:
                print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()