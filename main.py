import random


def hanging_out_cards():
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 5, 11] * 4
    random.shuffle(koloda)
    # print(koloda)
    return koloda


def black_jack():
    count = 0
    print("Let will 'Black Jack' play?")
    choice = input("Do you want take a card? (y/n)\n")
    while True:
        if choice == "y":
            current_card = hanging_out_cards().pop()
            print(f"Your card is: {current_card}")
            count += current_card
        elif choice == "n":
            print(f"You have score {count}. And it is all for you.")
            break
    print("By! The end of the game.")


if __name__ == "__main__":
    black_jack()
    # hanging_out_cards()
