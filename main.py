import random


def hanging_out_cards():
    koloda = [6, 7, 8, 9, 10, 2, 3, 4, 5, 11] * 4
    random.shuffle(koloda)
    # print(koloda)
    return koloda


def black_jack():
    print("Let will 'Black Jack' play?")
    current_card = hanging_out_cards().pop()
    print(f"Your card is: {current_card}")


if __name__ == "__main__":
    black_jack()
    # hanging_out_cards()
