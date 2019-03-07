game_list = []

while True:
    option = int(input("""
1 - Add a game,
2 - remove a game,
3 - insert a game.

Enter a choice 1,2, or 3
    """))
    if option == 1:
        print("this option allows you to add a game to your list")
        print(game_list)
        game = input("what game would you like to add to your list: ")
        game_list.append(game)
        print(game_list)
    elif option == 2:
        print("this option will allow you to remove a game from your list")
        print(game_list)

        while True:
            game = input("what game would you like to remove from your list: ")
            if game in game_list:
                game_list.remove(game)
                print(game_list)
                break
            else:
                print("that game is not on your list")

    elif option == 3:
        print("this option allows you to insert a game at a given position")
        game = input("what game would you like to insert in your list: ")
        while True:
            pos = int(input("at what position would you like to insert this game: "))
            pos -= 1
            if pos < len(game_list):
                game_list.insert(pos, game)
                print(game_list)
                break
            else:
                print("invalid position")
        
    if option == 4:
        input("press enter to exit")
        break
