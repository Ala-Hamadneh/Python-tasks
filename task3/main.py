def fibonacci(n):
    seq = [0, 1]
    for i in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def main():
    is_running = True
    seq=list()
    while is_running:
        print("\n" + "*" * 30)
        print("Fibonacci sequence")
        print("*" * 30)

        print("Enter 'q' to quit")
        choice = input("Enter the number of iterations for Fibonacci sequence: ")
        if choice.isdigit():
            seq=fibonacci(int(choice))
            print(f"The Fibonacci sequence of {choice} iterations is :",end =" ")
            for i in range(len(seq)):
                if i==len(seq):
                    print("")
                print(f"{seq[i]}", end ="")
                if i<len(seq)-1:
                    print(",", end ="")


        else:
            if choice =='q':
                is_running = False
                continue
            else :
                print(f"{choice} is not a number.")


if __name__ == "__main__":
    main()
