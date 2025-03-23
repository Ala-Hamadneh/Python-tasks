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

        choice = input("To quit press 'q' : ")
        if choice == "q":
            is_running = False
            continue
        else:
            continue


if __name__ == '__main__':
    main()