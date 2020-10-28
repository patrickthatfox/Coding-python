import numpy as np
import time

game_on = True

def create_board(n_rows, n_cols):
    return np.zeros((n_rows, n_cols))

def display_board(board):
    print("             __     __            __            __   ")
    print("     |       __|    __|   |_|    |__     |_       |  ")
    print("     |      |__     __|     |     __|    |_|      |  ")
    print("  ___________________________________________________")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + board[0][0]+"    |   "+board[0][1]+"   |  "+board[0][2]+"   |  "+board[0][3]+"   |  "+board[0][4]+"   |  "+board[0][5]+"   |  "+board[0][6]+"   |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + board[1][0]+"    |   "+board[1][1]+"   |  "+board[1][2]+"  |  "+board[1][3]+"  |  "+board[1][4]+"  |  "+board[1][5]+"  |  "+board[1][6]+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + board[2][0]+"   |   "+board[2][1]+"  |  "+board[2][2]+"  |  "+board[2][3]+"  |  "+board[2][4]+"  |  "+board[2][5]+"  |  "+board[2][6]+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + board[3][0]+"   |   "+board[3][1]+"  |  "+board[3][2]+"  |  "+board[3][3]+"  |  "+board[3][4]+"  |  "+board[3][5]+"  |  "+board[3][6]+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + board[4][0]+"   |   "+board[4][1]+"  |  "+board[4][2]+"  |  "+board[4][3]+"  |  "+board[4][4]+"  |  "+board[4][5]+"  |  "+board[4][6]+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  "+board[5][0]+"   |  "+board[5][1]+"   |  "+board[5][2]+"  |  "+board[5][3]+"  |  "+board[5][4]+"  |  "+board[5][5]+"  |  "+board[5][6]+"  |")
    print(" |_______|_______|______|______|______|______|______|")


def player_move(board, which_player):
    move = 9
    move = input("What position does player " + which_player + " play?")
    move = int(move)
    while move > 6 or move < 0:
        print("Please enter a number between 1 and 7")
        move = input("What position does player " + which_player + " play?")
    lookingforspace = True
    space_check = len(board)+1
    if which_player == "1":
        player_code = "x"
    elif which_player == "2":
        player_code = "o"
    else :
        print ("you need to enter 1 or 2")
        player_move(board, which_player)
    while lookingforspace:
        space_check -= 1
        if board[move][space_check] == 0:
            pos = space_check
            lookingforspace = False
    board[move][pos] = player_code
    return board

def check_win(board, player):
    cols = 0
    rows = 0
    rounds = 0
    checking = True
    while checking:
        if board[rows + rounds][cols] == "x":
            




board = create_board(6, 7)
player_move(board, "1")

while playing:
    display_board(board)
    time.sleep(1)
    player_move(board, "1")
    time.sleep(1)
    display_board(board)
    time.sleep(1)
    player_move(board, "2")
    time.sleep(1)



    
