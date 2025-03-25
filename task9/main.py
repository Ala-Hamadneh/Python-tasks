def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def fill_dict(dict_name):
    while True:
        key = input("\nEnter a key : ")
        value = input("Enter a value : ")
        dict_name[key] = value
        choice = input("\nEnter 'q' to quit filling: ")
        if choice == 'q':
            break

def main():
    is_running = True
    dict1= {}
    dict2= {}
    while is_running:
        print("\n" + "*" * 36)
        print("Merging Dictionaries ")
        print("*" * 36)
        choice = input("\nEnter 'q' to quit or 'c' to continue: ")
        if choice == 'q':
            is_running = False
            continue
        elif choice == 'c':
            print("\n" + "*" * 36)
            print("Filling the first dictionary")
            print("*" * 36)
            fill_dict(dict1)

            print("\n" + "*" * 36)
            print("Filling the second dictionary")
            print("*" * 36)
            fill_dict(dict2)
        else:
            print("invalid choice!")
    # be careful when using names merge_dicts <variable> with same function name = merge_dicts
    merged_dicts= merge_dicts(dict1, dict2)
    print(f"The merged dictionary is: {merged_dicts}")



if __name__ == "__main__":
    main()

