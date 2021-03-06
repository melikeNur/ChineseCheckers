import numpy as np
from strat_greedy import greedy
import pygame
import math

def build_board():

    board = np.zeros((17, 25))

    board[:][:] = -1

    board[0][12] = 1
    board[1][11] = 1
    board[1][13] = 1
    board[2][10] = 1
    board[2][12] = 1
    board[2][14] = 1
    board[3][9] = 1
    board[3][11] = 1
    board[3][13] = 1
    board[3][15] = 1

    board[4][18] = 2
    board[4][20] = 2
    board[4][22] = 2
    board[4][24] = 2
    board[5][19] = 2
    board[5][21] = 2
    board[5][23] = 2
    board[6][20] = 2
    board[6][22] = 2
    board[7][21] = 2

    board[9][21] = 3
    board[10][20] = 3
    board[10][22] = 3
    board[11][19] = 3
    board[11][21] = 3
    board[11][23] = 3
    board[12][18] = 3
    board[12][20] = 3
    board[12][22] = 3
    board[12][24] = 3

    board[13][9] = 4
    board[13][11] = 4
    board[13][13] = 4
    board[13][15] = 4
    board[14][10] = 4
    board[14][12] = 4
    board[14][14] = 4
    board[15][11] = 4
    board[15][13] = 4
    board[16][12] = 4

    board[9][21 - 18] = 5
    board[10][20 - 18] = 5
    board[10][22 - 18] = 5
    board[11][19 - 18] = 5
    board[11][21 - 18] = 5
    board[11][23 - 18] = 5
    board[12][18 - 18] = 5
    board[12][20 - 18] = 5
    board[12][22 - 18] = 5
    board[12][24 - 18] = 5

    board[4][18 - 18] = 6
    board[4][20 - 18] = 6
    board[4][22 - 18] = 6
    board[4][24 - 18] = 6
    board[5][19 - 18] = 6
    board[5][21 - 18] = 6
    board[5][23 - 18] = 6
    board[6][20 - 18] = 6
    board[6][22 - 18] = 6
    board[7][21 - 18] = 6

    board[4][8] = 0
    board[4][10] = 0
    board[4][12] = 0
    board[4][14] = 0
    board[4][16] = 0

    board[5][7] = 0
    board[5][9] = 0
    board[5][11] = 0
    board[5][13] = 0
    board[5][15] = 0
    board[5][17] = 0

    board[6][6] = 0
    board[6][8] = 0
    board[6][10] = 0
    board[6][12] = 0
    board[6][14] = 0
    board[6][16] = 0
    board[6][18] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[7][5] = 0
    board[7][7] = 0
    board[7][9] = 0
    board[7][11] = 0
    board[7][13] = 0
    board[7][15] = 0
    board[7][17] = 0
    board[7][19] = 0

    board[8][4] = 0
    board[8][6] = 0
    board[8][8] = 0
    board[8][10] = 0
    board[8][12] = 0
    board[8][14] = 0
    board[8][16] = 0
    board[8][18] = 0
    board[8][20] = 0

    board[9][5] = 0
    board[9][7] = 0
    board[9][9] = 0
    board[9][11] = 0
    board[9][13] = 0
    board[9][15] = 0
    board[9][17] = 0
    board[9][19] = 0

    board[10][6] = 0
    board[10][8] = 0
    board[10][10] = 0
    board[10][12] = 0
    board[10][14] = 0
    board[10][16] = 0
    board[10][18] = 0

    board[11][7] = 0
    board[11][9] = 0
    board[11][11] = 0
    board[11][13] = 0
    board[11][15] = 0
    board[11][17] = 0

    board[12][8] = 0
    board[12][10] = 0
    board[12][12] = 0
    board[12][14] = 0
    board[12][16] = 0

    return board


def build_invalid_set():

    player1_i_set = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14]]
    player2_i_set = [[9, 3], [10, 2], [10, 4], [11, 3], [11, 5], [12, 4], [12, 6]]
    player3_i_set = [[4, 4], [4, 6], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]
    player4_i_set = [[2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
    player5_i_set = [[4, 18], [4, 20], [5, 19], [5, 21], [6, 20], [6, 22], [7, 21]]
    player6_i_set = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [12, 18], [12, 20]]

    return player1_i_set, player2_i_set, player3_i_set, player4_i_set, player5_i_set, player6_i_set


def assign_invalid_set(player_turn, player1_i_set, player2_i_set, player3_i_set, player4_i_set, player5_i_set,
                       player6_i_set):

    invalid_set = player1_i_set

    if player_turn == 1:
        invalid_set = player1_i_set
    if player_turn == 2:
        invalid_set = player2_i_set
    if player_turn == 3:
        invalid_set = player3_i_set
    if player_turn == 4:
        invalid_set = player4_i_set
    if player_turn == 5:
        invalid_set = player5_i_set
    if player_turn == 6:
        invalid_set = player6_i_set

    return invalid_set

def get_row_col_from_mouse(board, all_legal_moves, obj_set, player_turn):
    obj_available = []
    for pos in obj_set:
        [x, y] = pos
        if board[x][y] != player_turn:
            obj_available.append([x, y])

    max_distance_metric = 0
    move_index = 0
    best_move = 0

    for move in all_legal_moves:

        [start_x, start_y] = move[0]
        [end_x, end_y] = move[1]

        for obj in obj_available:

            [obj_x, obj_y] = obj
            # trasform y coord thinking about the board as a square, which it should be
            square_start_y = (start_y * 14.43) / 25
            square_end_y = (end_y * 14.43) / 25
            square_obj_y = (obj_y * 14.43) / 25

            start_diag = math.sqrt(((obj_x - start_x) ** 2) + ((square_obj_y - square_start_y) ** 2))
            end_diag = math.sqrt(((obj_x - end_x) ** 2) + ((square_obj_y - square_end_y) ** 2))

            distance_travel = start_diag - end_diag
            distance_metric = distance_travel + start_diag * 0.5

            if distance_metric > max_distance_metric:
                best_move = move_index
                max_distance_metric = distance_metric

        move_index = move_index + 1
    return all_legal_moves[best_move]


def find_best_move(board, all_legal_moves, obj_set, player_turn, set_pieces, player1_set, player2_set, player3_set,
                   player4_set, player5_set, player6_set):

    obj_left = [i for i in obj_set + set_pieces if i not in obj_set or i not in set_pieces]
    if len(obj_left) == 2:
        for move in all_legal_moves:
            start_move = move[0]
            end_move = move[1]
            if start_move == obj_left[1] and end_move == obj_left[0]:
                return move
    try:

        if player_turn == 1:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 3:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 5:
           best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 2:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 4:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
        elif player_turn == 6:
            best_move = greedy(board, all_legal_moves, obj_set, player_turn)
            #print(best_move)
            #pos = pygame.mouse.get_pos()
            #x,y = pygame.mouse.get_pos()
            #best_moveX1 = input("X1")
            #best_moveX2 = input("X2")
            #best_moveY1 = input("Y1")
            #best_moveY2 = input("Y2")
            #print(best_moveX1,best_moveX2)
            #best_move=[[int(best_moveX1),int(best_moveX2)],[int(best_moveY1),int(best_moveY2)]]
            print(best_move)

    except Exception:
        return

    return best_move


def check_win(set_pieces, obj_set):

    game_end = True

    for piece in set_pieces:
        if piece not in obj_set:
            game_end = False

    return game_end
