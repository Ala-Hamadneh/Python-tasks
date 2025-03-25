def merge_lists(list1,list2):
    merged_list = []
// @alaa you can make merge as return list1 + list2
    for item in list1:
        merged_list.append(item)
    for item in list2:
        merged_list.append(item)
    return merged_list


def reverse_list(list_name):
    return list_name[::-1]

def fill_list(list_name):
    while True:
        value = input("\nEnter a value : ")
        list_name.append(value)
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break

def main():
    is_running = True
    list1= []
    list2= []
    while is_running:
        print("\n" + "*" * 40)
        print("Merging lists and reverse the merged list ")
        print("*" * 40)
        choice = input("\nEnter 'q' to quit or 'c' to continue: ")
        if choice == 'q':
            is_running = False
            continue
        elif choice == 'c':
            print("\n" + "*" * 40)
            print("Filling the first list")
            print("*" * 40)
            fill_list(list1)

            print("\n" + "*" * 40)
            print("Filling the second list")
            print("*" * 40)
            fill_list(list2)
        else:
            print("invalid choice!")

    merged_lists= merge_lists(list1, list2)
    print(f"The merged list is: {merged_lists}")
    reversed_list = reverse_list(merged_lists)
    print(f"the reversed list is  {reversed_list}")



if __name__ == "__main__":
    main()

