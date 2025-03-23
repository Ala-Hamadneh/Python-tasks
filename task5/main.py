import random

def main():
    is_running = True
    while is_running:
        print("\n" + "*" * 30)
        print("Random Number Generator")
        print("*" * 30)

        print("Enter 'q' to quit")
        choice = input("Enter the first number of the range: ")
        if choice.isdigit():
            num1=int(choice)

        else:
            if choice == 'q':
                is_running = False
                continue
            else:
                print(f"{choice} is not a number.")

        choice = input("Enter the second number of the range: ")
        if choice.isdigit():
            num2 = int(choice)
        else:
            if choice == 'q':
                is_running = False
                continue
            else:
                print(f"{choice} is not a number.")

        num = random.randint(num1, num2)
        print("*" * 30)
        print(f"The random number is {num}",end=" ")






if __name__ == '__main__':
    main()