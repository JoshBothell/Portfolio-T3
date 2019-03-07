#JoshBothell
#Tic Tac Toe
#12/18
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def instructions():
    print("""

    Welcome!
    Enter your input by choosing a number 0-8
    to place your X's or O's on the board
    
      0 ║ 1 ║ 2  
      ══╬═══╬══
      3 ║ 4 ║ 5
      ══╬═══╬══
      6 ║ 7 ║ 8


    Good luck beating me fleshbag.
""")

def yes_no(question):
    response = ""
    while response != "y" and response != "n":
        response = input(question)
    return response

def ask_number(question, low, high):
    """ASK FOR NUMBER WITHIN RANGE"""
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)

def pieces():
    go_first = yes_no("Would you like to go first? ")
    if go_first == "y":
        print("Coward")
        human = X
        computer = O
    else:
        print("I see the fleshbag has an ego...")
        human = O
        computer = X
    return human, computer

def new_board():
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display the board on the screen"""
    print("\n\t", board[0],"║", board[1], "║", board[2])
    print("\t", "══╬═══╬══          012")
    print("\t", board[3],"║", board[4], "║", board[5], "         345")
    print("\t", "══╬═══╬══          678")
    print("\t", board[6],"║", board[7], "║", board[8])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        else:
            continue
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_moves(board, human):
    moves = legal_moves(board)
    print(moves)
    move = None
    while move not in moves:
        move = ask_number("Enter the board position of your next move: ", 0, NUM_SQUARES)
        if move not in moves:
            print("That is not a valid move fleshbag...")
        elif move in moves:
            return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(winner, human, computer):
    if winner != TIE:
        print(winner, "WINS!")
    else:
        print("TIE")

    if winner == computer:
        print("You never had a chance fleshbag...")
    elif winner == human:
        print("fine, you win fleshbag.")
    elif winner == TIE:
        print("I would never let you win fleshbag")

def computer_moves(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("I will take square", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
        
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
        
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def main():
    while True:
        instructions()
        human, computer = pieces()
        turn = X
        board = new_board()
        display_board(board)
        while not winner(board):
            if turn == human:
                move = human_moves(board, human)
                board[move] = human
                display_board(board)
                turn = computer
            elif turn == computer:
                move = computer_moves(board, computer, human)
                board[move] = computer
                display_board(board)
                turn = human
        win = winner(board)
        congrat_winner(win, human, computer)
        play_again = input("Play Again? (y/n) ")
        if play_again == "y":
            continue
        else:
            break

main()
