

def main():
    strings = list()
    is_running = True

    print("\n" + "*" * 36)
    print("Stings Sorting in Alphabetical Order")
    print("*" * 36)

    while is_running:
        entered_string = input("Enter one word :")
        if entered_string.isalpha():
            strings.append(entered_string)
            print("\n" + "*" * 36)
            while True:
                choice = input("Enter 'q' to quit or 'c' to continue  :").lower()
                if choice == "q":
                    is_running = False
                    break
                elif choice == "c":
                    break
                else:
                    print("invalid choice!, try again.")
                    print("\n" + "*" * 36)
        else:
            print("String cant have numbers or any symbols try again.")
    strings.sort()
    print("The Sorted Words in Alphabetical Order are : ")
    for sting in strings:
        print(sting)


if __name__ == "__main__":
    main()