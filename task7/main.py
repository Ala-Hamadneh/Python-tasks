import string

def remove_punctuation(s):
    punc = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return s.translate(s.maketrans("","",punc))

def main():
    is_running = True
    while is_running:
        print("\n" + "*" * 35)
        print("Remove punctuations from a string.")
        print("*" * 35)
        text = input("Enter a string with punctuations : ")
        result = remove_punctuation(text)
        print(f"String without punctuation: {result}")

        while True:
            choice = input("Enter 'q' to quit or 'c' to continue  :").lower()
            if choice == "q":
                is_running = False
                break
            elif choice == "c":
                break
            else:
                print("invalid choice!, try again.")
                print("\n" + "*" * 36)


if __name__ == '__main__':
    main()