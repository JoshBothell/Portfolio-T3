# JoshBothell
# 2/19
import random
import time
import cards


def yes_no(question):
    """Asks the given question and repeats it until an answer is given in y/n format. the response is returned."""
    response = ""
    while response != "y" and response != "n":
        response = input(question)
    return response


def ask_num(num1, num2):
    """Asks for a number in a given range, includes error protection."""
    num_input = "Enter a number between " + str(num1) + " and " + str(num2) + ": "
    while True:
        num = input(num_input)
        if num.isdigit() and int(num) in range(num1, num2+1):
            return int(num)
        else:
            print("That is either outside of the range or not an integer.")


def roll(dice):
    """Rolls a dice with the given number of 'sides' and returns the number rolled."""
    dice_roll = random.randint(1, dice)
    return dice_roll


def switch_turn(num_players, turn):
    if turn < num_players - 1:
        turn += 1
    else:
        turn = 0
    return turn


def winner_congrats(winner):
    print("Congratulations!")
    print("...")
    time.sleep(1)
    print(winner, "is the winner!")


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = cards.Hand()

    def __str__(self):
        rep = self.name
        rep = rep + " " + str(self.hand.cards[0])
        return rep


if __name__ == "__main__":
    print("Your ran this module directly and did not 'import' it")
    input("\n\nPress the enter key to exit.")
