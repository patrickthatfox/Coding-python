import numpy as np
import time

game_on = True

def create_board(n_rows, n_cols):
    return np.zeros((n_rows, n_cols))

def display_board():
    print("             __     __            __            __   ")
    print("     |       __|    __|   |_|    |__     |_       |  ")
    print("     |      |__     __|     |     __|    |_|      |  ")
    print("  ___________________________________________________")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + f1+"    |   "+f2+"   |  "+f3+"   |  "+f4+"   |  "+f5+"   |  "+f6+"   |  "+f7+"   |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + f8+"    |   "+f9+"   |  "+f10+"  |  "+f11+"  |  "+f12+"  |  "+f13+"  |  "+f14+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + f15+"   |   "+f16+"  |  "+f17+"  |  "+f18+"  |  "+f19+"  |  "+f20+"  |  "+f21+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + f22+"   |   "+f23+"  |  "+f24+"  |  "+f25+"  |  "+f26+"  |  "+f27+"  |  "+f28+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  " + f29+"   |   "+f30+"  |  "+f31+"  |  "+f32+"  |  "+f33+"  |  "+f34+"  |  "+f35+"  |")
    print(" |_______|_______|______|______|______|______|______|")
    print(" |       |       |      |      |      |      |      |")
    print(" |  "+f36+"   |  "+f37+"   |  "+f38+"  |  "+f39+"  |  "+f40+"  |  "+f41+"  |  "+f42+"  |")
    print(" |_______|_______|______|______|______|______|______|")


def player_move(board, Which_player):
    move = input("What position does player " + Which_player + " play?")
    lookingforspace = True
    space_check = 7
    if Which_player = "1":
        player_code = "x"
    elif Which_player = "2":
        player_code = "o"
    while lookingforspace:
        space_check -= 1
        if board[move][space_check] == 0:
            pos = space_check
            lookingforspace = False
    board[move][pos] = player_code
    
