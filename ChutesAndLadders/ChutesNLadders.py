# Chutes and Ladders
# JoshBothell
# 1/19

import random
import time

EMPTY = " "
p1p = []
for i in range(0, 100):
    p1p.append(EMPTY)
p2p = []
for i in range(0, 100):
    p2p.append(EMPTY)
p3p = []
for i in range(0, 100):
    p3p.append(EMPTY)
p4p = []
for i in range(0, 100):
    p4p.append(EMPTY)


class Player (object):
    def __str__(self):
        strx = self.name + " is player number " + str(self.player_num)
        return strx

    def __init__(self, name, num):
        self.name = name
        self.player_num = num
        self.position = -1
        self.piece = self.name[0]

    def roll(self):
        roll = random.randint(1, 6)
        print("you rolled a", roll)
        return roll

    def move(self):
        move_roll = self.roll()
        if self.position + move_roll <= 99:
            old_pos = self.position
            self.position = self.position + move_roll
            if self.player_num == 1:
                p1p[old_pos] = EMPTY
                p1p[self.position] = self.piece
            elif self.player_num == 2:
                p2p[old_pos] = EMPTY
                p2p[self.position] = self.piece
            elif self.player_num == 3:
                p3p[old_pos] = EMPTY
                p3p[self.position] = self.piece
            elif self.player_num == 4:
                p4p[old_pos] = EMPTY
                p4p[self.position] = self.piece

    def win(self):
        if self.position == 99:
            return self.piece
        else:
            return None


class Board(object):
    def __init__(self):
        self.board = []

    def create_space(self):
        esp = Space(0)
        for i in range(100):
            self.board.append(esp)
        sp1 = Space(37)
        self.board[0] = sp1
        sp4 = Space(10)
        self.board[3] = sp4
        sp9 = Space(21)
        self.board[8] = sp9
        sp16 = Space(-10)
        self.board[15] = sp16
        sp21 = Space(21)
        self.board[20] = sp21
        sp28 = Space(56)
        self.board[27] = sp28
        sp51 = Space(16)
        self.board[50] = sp51
        sp56 = Space(-3)
        self.board[55] = sp56
        sp62 = Space(-52)
        self.board[61] = sp62
        sp64 = Space(-5)
        self.board[63] = sp64
        sp71 = Space(20)
        self.board[70] = sp71
        sp80 = Space(20)
        self.board[79] = sp80
        sp87 = Space(-63)
        self.board[86] = sp87
        sp93 = Space(-20)
        self.board[92] = sp93
        sp95 = Space(-20)
        self.board[94] = sp95
        sp98 = Space(-20)
        self.board[97] = sp98

    def display_board(self):
        print("╔══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╦══════╗")
        print(
            "║91" + p1p[90] + p2p[90] + "  ║92" + p1p[91] + p2p[91] + "  ║93" + p1p[92] + p2p[92] + "  ║94" + p1p[93] +
            p2p[93] + "  ║95" + p1p[94] + p2p[94] + "  ║96" + p1p[95] + p2p[95] + "  ║97" + p1p[96] + p2p[
                96] + "  ║98" + p1p[97] + p2p[97] + "  ║99" + p1p[98] + p2p[98] + "  ║100" + p1p[99] + p2p[99] + " ║ ")
        print(
            "║  " + p3p[90] + p4p[90] + "  ║  " + p3p[91] + p4p[91] + "  ║  " + p3p[92] + p4p[92] + "  ║  " + p3p[93] +
            p4p[93] + "  ║  " + p3p[94] + p4p[94] + "  ║  " + p3p[95] + p4p[95] + "  ║  " + p3p[96] + p4p[
                96] + "  ║  " + p3p[97] + p4p[97] + "  ║  " + p3p[98] + p4p[98] + "  ║   " + p3p[99] + p4p[99] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║90" + p1p[89] + p2p[89] + "  ║89" + p1p[88] + p2p[88] + "  ║88" + p1p[87] + p2p[87] + "  ║87" + p1p[86] +
            p2p[86] + "  ║86" + p1p[85] + p2p[85] + "  ║85" + p1p[84] + p2p[84] + "  ║84" + p1p[83] + p2p[
                83] + "  ║83" + p1p[82] + p2p[82] + "  ║82" + p1p[81] + p2p[81] + "  ║ 81" + p1p[80] + p2p[80] + " ║ ")
        print(
            "║  " + p3p[89] + p4p[89] + "  ║  " + p3p[88] + p4p[88] + "  ║  " + p3p[87] + p4p[87] + "  ║  " + p3p[86] +
            p4p[86] + "  ║  " + p3p[85] + p4p[85] + "  ║  " + p3p[84] + p4p[84] + "  ║  " + p3p[83] + p4p[
                83] + "  ║  " + p3p[82] + p4p[82] + "  ║  " + p3p[81] + p4p[81] + "  ║   " + p3p[80] + p4p[80] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║71" + p1p[70] + p2p[70] + "  ║72" + p1p[71] + p2p[71] + "  ║73" + p1p[72] + p2p[72] + "  ║74" + p1p[73] +
            p2p[73] + "  ║75" + p1p[74] + p2p[74] + "  ║76" + p1p[75] + p2p[75] + "  ║77" + p1p[76] + p2p[
                76] + "  ║78" + p1p[77] + p2p[77] + "  ║79" + p1p[78] + p2p[78] + "  ║ 80" + p1p[79] + p2p[79] + " ║ ")
        print(
            "║  " + p3p[70] + p4p[70] + "  ║  " + p3p[71] + p4p[71] + "  ║  " + p3p[72] + p4p[72] + "  ║  " + p3p[73] +
            p4p[73] + "  ║  " + p3p[74] + p4p[74] + "  ║  " + p3p[75] + p4p[75] + "  ║  " + p3p[76] + p4p[
                76] + "  ║  " + p3p[77] + p4p[77] + "  ║  " + p3p[78] + p4p[78] + "  ║   " + p3p[79] + p4p[79] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║70" + p1p[69] + p2p[69] + "  ║69" + p1p[68] + p2p[68] + "  ║68" + p1p[67] + p2p[67] + "  ║67" + p1p[66] +
            p2p[66] + "  ║66" + p1p[65] + p2p[65] + "  ║65" + p1p[64] + p2p[64] + "  ║64" + p1p[63] + p2p[
                63] + "  ║63" + p1p[62] + p2p[62] + "  ║62" + p1p[61] + p2p[61] + "  ║ 61" + p1p[60] + p2p[60] + " ║ ")
        print(
            "║  " + p3p[69] + p4p[69] + "  ║  " + p3p[68] + p4p[68] + "  ║  " + p3p[67] + p4p[67] + "  ║  " + p3p[66] +
            p4p[66] + "  ║  " + p3p[65] + p4p[65] + "  ║  " + p3p[64] + p4p[64] + "  ║  " + p3p[63] + p4p[
                63] + "  ║  " + p3p[62] + p4p[62] + "  ║  " + p3p[61] + p4p[61] + "  ║   " + p3p[60] + p4p[60] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║51" + p1p[50] + p2p[50] + "  ║52" + p1p[51] + p2p[51] + "  ║53" + p1p[52] + p2p[52] + "  ║54" + p1p[53] +
            p2p[53] + "  ║55" + p1p[54] + p2p[54] + "  ║56" + p1p[55] + p2p[55] + "  ║57" + p1p[56] + p2p[
                56] + "  ║58" + p1p[57] + p2p[57] + "  ║59" + p1p[58] + p2p[58] + "  ║ 60" + p1p[59] + p2p[59] + " ║ ")
        print(
            "║  " + p3p[50] + p4p[50] + "  ║  " + p3p[51] + p4p[51] + "  ║  " + p3p[52] + p4p[52] + "  ║  " + p3p[53] +
            p4p[53] + "  ║  " + p3p[54] + p4p[54] + "  ║  " + p3p[55] + p4p[55] + "  ║  " + p3p[56] + p4p[
                56] + "  ║  " + p3p[57] + p4p[57] + "  ║  " + p3p[58] + p4p[58] + "  ║   " + p3p[59] + p4p[59] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║50" + p1p[49] + p2p[49] + "  ║49" + p1p[48] + p2p[48] + "  ║48" + p1p[47] + p2p[47] + "  ║47" + p1p[46] +
            p2p[46] + "  ║46" + p1p[45] + p2p[45] + "  ║45" + p1p[44] + p2p[44] + "  ║44" + p1p[43] + p2p[
                43] + "  ║43" + p1p[42] + p2p[42] + "  ║42" + p1p[41] + p2p[41] + "  ║ 41" + p1p[40] + p2p[40] + " ║ ")
        print(
            "║  " + p3p[49] + p4p[49] + "  ║  " + p3p[48] + p4p[48] + "  ║  " + p3p[47] + p4p[47] + "  ║  " + p3p[46] +
            p4p[46] + "  ║  " + p3p[45] + p4p[45] + "  ║  " + p3p[44] + p4p[44] + "  ║  " + p3p[43] + p4p[
                43] + "  ║  " + p3p[42] + p4p[42] + "  ║  " + p3p[41] + p4p[41] + "  ║   " + p3p[40] + p4p[40] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║31" + p1p[30] + p2p[30] + "  ║32" + p1p[31] + p2p[31] + "  ║33" + p1p[32] + p2p[32] + "  ║34" + p1p[33] +
            p2p[33] + "  ║35" + p1p[34] + p2p[34] + "  ║36" + p1p[35] + p2p[35] + "  ║37" + p1p[36] + p2p[
                36] + "  ║38" + p1p[37] + p2p[37] + "  ║39" + p1p[38] + p2p[38] + "  ║ 40" + p1p[39] + p2p[39] + " ║ ")
        print(
            "║  " + p3p[30] + p4p[30] + "  ║  " + p3p[31] + p4p[31] + "  ║  " + p3p[32] + p4p[32] + "  ║  " + p3p[33] +
            p4p[33] + "  ║  " + p3p[34] + p4p[34] + "  ║  " + p3p[35] + p4p[35] + "  ║  " + p3p[36] + p4p[
                36] + "  ║  " + p3p[37] + p4p[37] + "  ║  " + p3p[38] + p4p[38] + "  ║   " + p3p[39] + p4p[39] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║30" + p1p[29] + p2p[29] + "  ║29" + p1p[28] + p2p[28] + "  ║28" + p1p[27] + p2p[27] + "  ║27" + p1p[26] +
            p2p[26] + "  ║26" + p1p[25] + p2p[25] + "  ║25" + p1p[24] + p2p[24] + "  ║24" + p1p[23] + p2p[
                23] + "  ║23" + p1p[22] + p2p[22] + "  ║22" + p1p[21] + p2p[21] + "  ║ 21" + p1p[20] + p2p[20] + " ║ ")
        print(
            "║  " + p3p[29] + p4p[29] + "  ║  " + p3p[28] + p4p[28] + "  ║  " + p3p[27] + p4p[27] + "  ║  " + p3p[26] +
            p4p[26] + "  ║  " + p3p[25] + p4p[25] + "  ║  " + p3p[24] + p4p[24] + "  ║  " + p3p[23] + p4p[
                23] + "  ║  " + p3p[22] + p4p[22] + "  ║  " + p3p[21] + p4p[21] + "  ║   " + p3p[20] + p4p[20] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print(
            "║11" + p1p[10] + p2p[10] + "  ║12" + p1p[11] + p2p[11] + "  ║13" + p1p[12] + p2p[12] + "  ║14" + p1p[13] +
            p2p[13] + "  ║15" + p1p[14] + p2p[14] + "  ║16" + p1p[15] + p2p[15] + "  ║17" + p1p[16] + p2p[
                16] + "  ║18" + p1p[17] + p2p[17] + "  ║19" + p1p[18] + p2p[18] + "  ║ 20" + p1p[19] + p2p[19] + " ║ ")
        print(
            "║  " + p3p[10] + p4p[10] + "  ║  " + p3p[11] + p4p[11] + "  ║  " + p3p[12] + p4p[12] + "  ║  " + p3p[13] +
            p4p[13] + "  ║  " + p3p[14] + p4p[14] + "  ║  " + p3p[15] + p4p[15] + "  ║  " + p3p[16] + p4p[
                16] + "  ║  " + p3p[17] + p4p[17] + "  ║  " + p3p[18] + p4p[18] + "  ║   " + p3p[19] + p4p[19] + " ║ ")
        print("╠══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╬══════╣")
        print("║10" + p1p[9] + p2p[9] + "  ║ 9" + p1p[8] + p2p[8] + "  ║ 8" + p1p[7] + p2p[7] + "  ║ 7" + p1p[6] + p2p[
            6] + "  ║ 6" + p1p[5] + p2p[5] + "  ║ 5" + p1p[4] + p2p[4] + "  ║ 4" + p1p[3] + p2p[3] + "  ║ 3" + p1p[2] +
              p2p[2] + "  ║ 2" + p1p[1] + p2p[1] + "  ║ 1" + p1p[0] + p2p[0] + "  ║ ")
        print("║  " + p3p[9] + p4p[9] + "  ║  " + p3p[8] + p4p[8] + "  ║  " + p3p[7] + p4p[7] + "  ║  " + p3p[6] + p4p[
            6] + "  ║  " + p3p[5] + p4p[5] + "  ║  " + p3p[4] + p4p[4] + "  ║  " + p3p[3] + p4p[3] + "  ║  " + p3p[2] +
              p4p[2] + "  ║  " + p3p[1] + p4p[1] + "  ║  " + p3p[0] + p4p[0] + "  ║ ")
        print("╚══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╩══════╝")


class Space(object):
    def __init__(self, move):
        self.move = move

    def move_player(self, player, board):
        oldpos = player.position
        player.position = player.position + self.move
        time.sleep(0.5)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        if self.move > 0:
            print("This space has a ladder, " + player.piece + " moves up " + str(self.move) + " spaces.")
            input("Press enter to use the ladder.")
        elif self.move < 0:
            print("This space has a chute, " + player.piece + " moves down " + str(self.move) + " spaces.")
            input("Press enter to use the chute.")
        if self.move > 0 or self.move < 0:
            if player.player_num == 1:
                p1p[oldpos] = EMPTY
                p1p[player.position] = player.piece
            elif player.player_num == 2:
                p2p[oldpos] = EMPTY
                p2p[player.position] = player.piece
            elif player.player_num == 3:
                p3p[oldpos] = EMPTY
                p3p[player.position] = player.piece
            elif player.player_num == 4:
                p4p[oldpos] = EMPTY
                p4p[player.position] = player.piece
        board.display_board()


def ask_num(num1, num2):
    num_input = "Enter a number between " + str(num1) + " and " + str(num2) + ": "
    while True:
        num = input(num_input)
        if num.isdigit() and int(num) in range(num1, num2+1):
            return int(num)
        else:
            print("That is either outside of the range or not an integer.")


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


def main():
    print("How many people are playing?")
    num_players = ask_num(2, 4)
    players = []
    turn = 0
    winner = None
    for i in range(num_players):
        print("player", i+1)
        name = input("Enter your name: ")
        name = name.title()
        player = Player(name, i+1)
        players.append(player)
    board = Board()
    board.create_space()
    while not winner:
        print(players[turn].name + ", it is your turn, you are on spot " + str(players[turn].position + 1))
        input("press enter to roll")
        players[turn].move()
        playpos = players[turn].position
        space = board.board[playpos]
        space.move_player(players[turn], board)
        winner = players[turn].win()
        if not winner:
            turn = switch_turn(num_players, turn)
    winner_congrats(winner)


main()
input("Press enter to quit... ")
