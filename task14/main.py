
def fill_list(list_name):
    while True:
        if is_first:
            value = input("\nEnter a value to the keys list: ")
        else:
            value = input("\nEnter a value to the values list: ")
        list_name.append(value)
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break

def convert_lists_to_dict(list1,list2):
    return dict(zip(list1,list2))


def main():
    is_running = True
    global is_first
    keys=[]
    values=[]
    while is_running:
        print("\n" + "*" * 35)
        print("Convert Lists to Dict")
        print("*" * 35)
        choice=input("\nEnter 'q' to quit : ")
        if choice == 'q':
            is_running=False
            continue
        else:
            print("Filling the first list")
            is_first = True
            fill_list(keys)
            print("Filling the second list")
            is_first = False
            fill_list(values)
            print("\n" + "*" * 35)
            print("Convert Lists to Dict")
            print("*" * 35)
            dict1=convert_lists_to_dict(keys,values)
            print(f"The resulted dict is {dict1} ")


if __name__ == '__main__':
    main()