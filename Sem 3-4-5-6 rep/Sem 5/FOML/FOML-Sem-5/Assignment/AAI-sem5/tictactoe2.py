"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
import numpy as np

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    for x in board[:]:
        for unit in x:
            X_count = X_count + int(unit=="X")
            O_count = O_count + int(unit=="O")
 
    if X_count == O_count:
        return "X"
    elif X_count > O_count:
        return "O"
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []
    for row,x in enumerate(board):
        for col,unit in enumerate(x):
            if unit==None:
                possible_actions.append((row, col))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x,y) = action
    dummy = deepcopy(board)
    if dummy[x][y] == None:
        dummy[x][y] = player(board)
    else:
        raise Exception("Invalid Move")
        
    return dummy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:        #Checking row wins
        if sum(unit== "X" for unit in row) ==3:
            #print("row wise")
            return "X"
        elif sum(unit=="O" for unit in row) ==3:
            #print("row wise")
            return "O"
    
    for i in [0,1,2]:       #Checking column wins
        if sum(row[i]== "X" for row in board) ==3:
            #print("col wise")
            return "X"
        
        if sum(row[i]== "O" for row in board) ==3:
            #print("col wise")
            return "O"
        
    if sum([board[0][0]=="X", board[1][1]=="X", board[2][2]=="X"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 1")
        return "X"
    
    if sum([board[0][2]=="X", board[1][1]=="X", board[2][0]=="X"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 2")
        return "X"
    
    if sum([board[0][0]=="O", board[1][1]=="O", board[2][2]=="O"]) ==3:
        #print("dia wise 3")
        return "O"
    
    if sum([board[0][2]=="O", board[1][1]=="O", board[2][0]=="O"]) ==3:      #Checking Diagonal Wins
        #print("dia wise 4")
        return "O"
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    None_count=0
    for row in board:
        None_count = None_count + sum(unit==None for unit in row)
    
    if None_count == 0 or winner(board)!=None:
            return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        
        '''
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move
        '''
            
    return v, move

def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        '''
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move
        '''

 

    return v, move
# print(actions([[None, 1, 0], [0, 1, 1], [1, None, 0]]))