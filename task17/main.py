def main():
    is_running = True
    file = open('names.txt', 'r+')
    while is_running:
        print("\n"+"*"*35)
        print('File Read & Write Handling  ')
        print("1- read & print all the lines from the file 'names.txt'")
        print("2- read & print the first line of 'names.txt'")
        print("3- write to the file 'names.txt'")
        print("4- close the file 'names.txt'")
        print("*"*35)
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                file.seek(0)
                print(file.read())
            case '2':
                file.seek(0)
                print(file.readline())
            case '3':
                file.seek(0,2)
                name=input("Enter a name to add it to the file 'names.txt': ")
                file.write("\n"+name)
            case '4':
                is_running = False
                file.close()
            case _:
                print("Invalid choice. Try again.")


    file.close()

if __name__ == '__main__':
    main()