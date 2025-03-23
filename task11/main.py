def list_slicing(lst):
    start_index = int(input("Enter the start index : "))
    end_index = int(input("Enter end index : "))
    if end_index > len(lst):
        end_index = len(lst)
    if start_index > end_index:
        print("\nThe starting index is greater than the ending index.")
        return list_slicing(lst)
    return lst[start_index:end_index]

def fill_list(list_name):
    while True:
        value = input("\nEnter a value : ")
        list_name.append(value)
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break


def main():
    is_running = True
    my_list=[]
    while is_running:
        print("\n" + "*" * 30)
        print("List Slicing ")
        print("*" * 30)
        choice = input("\nEnter 'q' to quit or 'c' to continue: ")
        if choice == 'c':
            fill_list(my_list)
            print(list_slicing(my_list))
            continue
        elif choice == 'q':
            is_running = False
            continue
        else:
            print("invalid choice!")



if __name__ == '__main__':
    main()