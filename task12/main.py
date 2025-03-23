def remove_duplicates(list_name):
    return list(set(list_name))

def fill_list(list_name):
    while True:
        value = input("\nEnter a value : ")
        list_name.append(value)
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break

def main():
    is_running = True
    my_list = []
    while is_running:
        print("\n" + "*" * 35)
        print("Removing Duplicates from a List")
        print("*" * 35)
        choice = input("\nEnter 'q' to quit or 'c' to continue: ")
        if choice == 'c':
            fill_list(my_list)
            my_list=remove_duplicates(my_list)
            print(f"The list is now {my_list}")
            continue
        elif choice == 'q':
            is_running = False
            continue
        else:
            print("invalid choice!")

if __name__ == '__main__':
    main()