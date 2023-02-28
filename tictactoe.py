#import the numpy library
import numpy as np

#create a 3x3 board
board = np.array([['-','-','-'],['-','-','-'],['-','-','-']])

#define a function to print the board
def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print()

#define a function to check if the game is won
def check_win(board):
    #check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return True
    #check for vertical wins
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True
    #check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True
    return False

#define a function to make a move
def make_move(board, row, col, player):
    board[row][col] = player
    return board

#define a function to check if a move is valid
def valid_move(board, row, col):
    if board[row][col] == '-':
        return True
    else:
        return False

#define the main game loop
player = 'X'
while True:
    #print the board
    print_board(board)
    #get player input
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
    #check if the move is valid
    if valid_move(board, row, col):
        #make the move
        board = make_move(board, row, col, player)
        #check if the game is won
        if check_win(board):
            print_board(board)
            print('Player ' + player + ' wins!')
            break
        #switch players
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print('Invalid move!')