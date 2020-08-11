import random
import constants as c
from constants import game_size

def start_game():
    game_matrix = [[0 for j in range(game_size)] for i in range(game_size)]
    return game_matrix

def add_random_2(game_matrix):
    row = random.randint(0,3)
    column = random.randint(0,3)

    while(game_matrix[row][column] != 0):
        row = random.randint(0,3)
        column = random.randint(0,3)
    
    game_matrix[row][column] = 2

def check_current_state(game_matrix):
    #chech for won
    for row in range(game_size):
        for col in range(game_size):
            if game_matrix[row][col] == c.win_number:
                return "WON"
    
    #check for in-game
    for row in range(game_size):
        for col in range(game_size):
            if game_matrix[row][col] == 0:
                return "Game Not Over"

    for row in range(game_size-1):
        for col in range(game_size-1):
            if (game_matrix[row][col] == game_matrix[row+1][col]) or (game_matrix[row][col] == game_matrix[row][col+1]):
                return "Game Not Over"
    
    for col in range(game_size-1):
        if game_matrix[game_size-1][col] == game_matrix[game_size-1][col+1]:
            return "Game Not Over"
    
    for row in range(game_size-1):
        if game_matrix[row][game_size-1] == game_matrix[row+1][game_size-1]:
            return "Game Not Over"
    
    #check for lost
    return "LOST"

def compress_game_matrix(game_matrix):
    new_game_matrix = [[0 for j in range(game_size)] for i in range(game_size)]
    ischanged = False

    for row in range(game_size):
        pos = 0
        for col in range(game_size):
            if game_matrix[row][col] != 0:
                new_game_matrix[row][pos] = game_matrix[row][col]
                if col != pos:                                     #this means a change is happening because col and pos are goin parallel
                    ischanged = True
                pos += 1
    
    return new_game_matrix,ischanged

def merge_game_matrix(game_matrix):

    ischanged = False
    for row in range(game_size):
        for col in range(game_size-1):
            if game_matrix[row][col] == game_matrix[row][col+1] and game_matrix[row][col] != 0:
                game_matrix[row][col] *= 2
                game_matrix[row][col+1] = 0
                ischanged = True
    
    return game_matrix,ischanged

def reverse_game_matrix(game_matrix):
    new_game_matrix = []

    for row in range(game_size):
        new_game_matrix.append(game_matrix[row][::-1])
    
    return new_game_matrix

def transpose_game_matrix(game_matrix):
    new_game_matrix = [[0 for j in range(game_size)] for i in range(game_size)]

    for row in range(game_size):
        for col in range(game_size):
            new_game_matrix[col][row] = game_matrix[row][col]

    return new_game_matrix

def left_move(game_matrix):
    game_matrix,ischanged1 = compress_game_matrix(game_matrix)
    game_matrix,ischanged2 = merge_game_matrix(game_matrix)
    ischanged = ischanged1 or ischanged2
    game_matrix,temp = compress_game_matrix(game_matrix)

    return game_matrix,ischanged

def right_move(game_matrix):
    game_matrix = reverse_game_matrix(game_matrix)
    game_matrix,ischanged1 = compress_game_matrix(game_matrix)
    game_matrix,ischanged2 = merge_game_matrix(game_matrix)
    ischanged = ischanged1 or ischanged2
    game_matrix,temp = compress_game_matrix(game_matrix)
    game_matrix = reverse_game_matrix(game_matrix)

    return game_matrix,ischanged

def up_move(game_matrix):
    game_matrix = transpose_game_matrix(game_matrix)
    game_matrix,ischanged1 = compress_game_matrix(game_matrix)
    game_matrix,ischanged2 = merge_game_matrix(game_matrix)
    ischanged = ischanged1 or ischanged2
    game_matrix,temp = compress_game_matrix(game_matrix)
    game_matrix = transpose_game_matrix(game_matrix)

    return game_matrix,ischanged

def down_move(game_matrix):
    game_matrix = transpose_game_matrix(game_matrix)
    game_matrix = reverse_game_matrix(game_matrix)
    game_matrix,ischanged1 = compress_game_matrix(game_matrix)
    game_matrix,ischanged2 = merge_game_matrix(game_matrix)
    ischanged = ischanged1 or ischanged2
    game_matrix,temp = compress_game_matrix(game_matrix)
    game_matrix = reverse_game_matrix(game_matrix)
    game_matrix = transpose_game_matrix(game_matrix)

    return game_matrix,ischanged


