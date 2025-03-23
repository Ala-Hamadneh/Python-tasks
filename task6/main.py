import itertools
import random
from random import choices


def main():
    card_type = ["Heart", "Spade", "Diamond", "Club"]
    cards_deck = list(itertools.product(card_type, range(1, 14)))

    is_running = True
    while is_running:
        print("\n" + "*" * 30)
        print("Shuffling the cards...")
        print("*" * 30)

        choice = input("Enter 'q' to quit , 'c' to shuffle the cards: " )
        if choice == "q":
            is_running = False
            continue
        elif choice == "c":
            random.shuffle(cards_deck)
            c=0
            for value, suit in cards_deck:
                match suit:
                    case 1:
                        suit='Ace'
                    case 11:
                        suit='Jack'
                    case 12:
                        suit='Queen'
                    case 13:
                        suit='King'

                print(f"{suit} of {value}")
                c+=1
                if c == 13:
                    print("\n" + "*" * 30)
                    c=0
        else:
            print("Invalid choice.")









if __name__ == '__main__':
    main()