# JoshBothell
# 2/19
import games, random, cards


deck = cards.Deck()
deck.populate()
deck.shuffle()

print("Welcome to the simple high card game!")

again = None
while again != "n":
    players = list([])
    print("How many players?")
    num = games.ask_num(2, 11)
    for i in range(num):
        name = input("Player name: ")
        player = games.Player(name)
        players.append(player)
    hands = list([])
    for player in players:
        hand = player.hand
        hands.append(hand)
    deck.deal(hands, 1)
    print("Here are the results: ")
    for player in players:
        print(player)
    again = games.yes_no("Do you want to play again? (y/n): ")
input("Press enter to exit.")
