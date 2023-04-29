# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:17:08 2022

@author: Hol-IT

"
  1 2 3
1 _|_|_
2 _|_|_
3  | |
"""

#import random

board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "]]
player = ["X", "O"]
x = 0
winner = None

def display_board(board):        
    print("  1 2 3")
    for i in range(len(board)):
        print(i+1, end=" ")
        if i < 2: 
            for j in range(len(board[i])):
                if j < 2:
                    if board[i][j] == " ":
                        print("_", end="|")
                    else:
                        print(board[i][j], end="|")
                else:
                    if board[i][j] == " ":
                        print("_")
                    else:
                        print(board[i][j])
        else:
            for j in range(len(board[i])):
                if j < 2:
                    print(board[i][j], end="|")
                else:
                    print(board[i][j])
                    
def is_win(board):
    # horizontal
    for b in board:
        if b[0] != " " and b.count(b[0]) == 3:
            return b[0]
    
    # vertikal
    for i in range(len(board)):
        b = [board[0][i], board[1][i], board[2][i]]
        if b[0] != " " and b.count(b[0]) == 3:
            return b[0]
    
    # diagonal
    b = [board[0][0], board[1][1], board[2][2]]
    if b[0] != " " and b.count(b[0]) == 3:
        return b[0]

    b = [board[0][2], board[1][1], board[2][0]]
    if b[0] != " " and b.count(b[0]) == 3:
        return b[0]

def is_full(board):
    for b in board:
        if b.count(" ") > 0:
            return False
    return True

def bestMove(board):
    bestScore = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = [i+1, j+1]
    
    return move

scores = {"X" : -1, "O" : 1}

def minimax(board, isMaximizing):
    full = is_full(board)
    result = is_win(board)
    if result == None:
        if full == True:
            return 0
    else:
        return scores[result]

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
        
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    bestScore = min(score, bestScore)
        
        return bestScore
    

print("Welcome to Tictactoe!")
print("Mode Permainan :\n1. Multiplayer\n2. vs. Comp")
try:
    game_mode = int(input("Silahkan Pilih Mode Permainan : "))
except Exception as e:
    print(e)

        
while x < 9 and not winner == None:
    valid = False
    display_board(board)
    print("")
    print("Player ", player[x%2])
    while not valid:
        if game_mode == 2 and x%2 == 1:
            move = bestMove(board) 
            baris = move[0]
            kolom = move[1]
        else:
            baris = int(input("silahkan pilih baris : "))
            kolom = int(input("silahkan pilih kolom : "))
    
        if board[baris-1][kolom-1] == " ":
            board[baris-1][kolom-1] = player[x%2]
            valid = True
        else:
            print("maaf baris dan kolom sudah terisi")
            
        full = is_full(board)
        winner = is_win(board)
        if winner == None:
            if full == True:
                print('game FRAW')
        else:
            print('game dimenangkan oleh ', winner)
    #win = is_win(board)
    
    x += 1
    
display_board(board)                    

#print("  1 2 3")
#print("1 _|_|_")
#print("2 _|_|_")
#print("3 _|_|_")