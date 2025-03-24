def fill_dict(dict_name):
    while True:
        print("Enter the key and the value , to quit press 'q':")
        key = input("Key :")
        value = input("Value :")
        if key == "q" or value == "q":
            break
        else:
            dict_name[key] = value



def delete_key(dict_name, key):
    if key in dict_name:
        del dict_name[key]
    else:
        print("Key not found!")
    return dict_name


def main():
    is_running = True
    dict_name = {}
    while is_running:
        print("\n" + "*" * 45)
        print("Delete an Element from dictionary if exists")
        print("*" * 45)
        print("Filling the Dictionary \n")
        fill_dict(dict_name)
        print("\n" + "*" * 45)
        print("Enter the key to remove the element :")
        print("*" * 45)
        key = input("Key :")
        dict_name = delete_key(dict_name, key)
        print("=" * 45)
        choice=input("To quit press 'q' or to continue press 'c':")
        print("=" * 45)
        if choice == "q":
            is_running = False
            print("\n" + "*" * 45)
            print(dict_name)
            print("*" * 45)
            continue
        elif choice == "c":
            print("\n" + "*" * 45)
            print(dict_name)
            print("*" * 45)
            continue






if __name__ == '__main__':
    main()
