
def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0: #if num % ((num^0.5 )+1) == 0
            return False
        else:
            return True



def main():
    is_running = True
    while is_running:
        print("\n" + "*" * 30)
        print("Prime Number Checker")
        print("*" * 30)
        print("1. Check if a number is prime")
        print("2. Quit")
        print("*" * 30)


        choice = input("\nEnter your choice (1 or 2): ")

        if choice == "1":
            num = input("\nEnter a number: ")
            if num.isdigit():
                num = int(num)
                if prime_num(num):
                    print(f"\n{num} is a prime number.")
                else:
                    print(f"\n{num} is not a prime number.")
            else:
                print("\nInvalid input! Please enter a valid number.")
        elif choice == "2":
            is_running = False
        else:
            print("\nInvalid choice! Please enter 1 or 2.")




if __name__ == "__main__":
    main()