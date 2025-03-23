def fill_list(list_name):
    while True:
        value = input("\nEnter a value: ")
        list_name.append(value)
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break

def delete_element(list_name):
    try:
        index = int(input("\nEnter the index of the element to delete: "))
        del list_name[index]
        print(f"Element at index {index} deleted.")
    except (IndexError, ValueError):
        print("Invalid index! Please enter a valid index.")

def remove_value(list_name):
    value = input("\nEnter the value to remove: ")
    if value in list_name:
        list_name.remove(value)
        print(f"First occurrence of {value} removed.")
    else:
        print(f"{value} not found in the list.")

def pop_element(list_name):
    try:
        index = int(input("\nEnter the index of the element to pop: "))
        popped_value = list_name.pop(index)
        print(f"Element at index {index} popped. Popped value: {popped_value}")
    except (IndexError, ValueError):
        print("Invalid index! Please enter a valid index.")

def main():
    is_running = True
    my_list = []
    while is_running:
        print("\n" + "*" * 35)
        print("List Operations Menu")
        print("*" * 35)
        print("1. Fill the list")
        print("2. Delete element by index")
        print("3. Remove element by value")
        print("4. Pop element by index")
        print("5. Display the list")
        print("6. Quit")
        print("*" * 35)

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            fill_list(my_list)
        elif choice == "2":
            delete_element(my_list)
        elif choice == "3":
            remove_value(my_list)
        elif choice == "4":
            pop_element(my_list)
        elif choice == "5":
            print("\nCurrent list:", my_list)
        elif choice == "6":
            is_running = False
            continue
        else:
            print("\nInvalid choice!")



if __name__ == '__main__':
    main()