import random


def hanging_out_cards():
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 5, 11] * 4
    random.shuffle(koloda)
    # print(koloda)
    return koloda


def black_jack():
    aim = 21
    count = 0
    print("Let will 'Black Jack' play?")
    while True:
        choice = input("Do you want take a card? (y/n)\n")
        if choice == "y":
            current_card = hanging_out_cards().pop()
            count += current_card
            print(f"Your card is: {current_card}")
            if count > aim:
                print(f"You lost! The score is: {count}.")
                break
            elif count == aim:
                print(f"You win! The score is: {count}.")
                break
            else:
                print(f"You have {count} scores.")
        elif choice == "n":
            print(f"You have score {count}. And it is all for you.")
            break
    print("By! The end of the game.")


if __name__ == "__main__":
    black_jack()
