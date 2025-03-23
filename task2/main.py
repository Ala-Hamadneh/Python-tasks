
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    is_running = True
    while is_running:
        print("\n" + "*" * 30)
        print("Factorial Of Number")
        print("*" * 30)

        print("Enter 'q' to quit")
        choice = input("Enter the number you are looking for it's Factorial: ")
        if choice.isdigit():
            factorial(int(choice))
            print(f"The Factorial of {choice} is {factorial(int(choice))}")
        else:
            if choice =='q':
                is_running = False
                continue
            else :
                print(f"{choice} is not a number.")


if __name__ == "__main__":
    main()