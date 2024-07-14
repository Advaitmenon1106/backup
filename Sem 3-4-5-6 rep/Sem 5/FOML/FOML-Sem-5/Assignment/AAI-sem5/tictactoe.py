from copy import deepcopy

empty = None

def initialise():
    board = []
    row = []
    for i in range (0, 3):
        for j in range(0, 3):
            row.append(empty)
        board.append(row)
        row = []
    
    return board

def player(board):
    countOfX = 0
    countOfY = 0
    for row in range (0, 3):
        for col in range (0, 3):
            if board[row][col] == 1:
                countOfX+=1
            elif board[row][col] == 0:
                countOfY+=1
    if countOfX>countOfY:
        return 'O'
    elif countOfX==countOfY:
        return 'X'

def actions(board):
    possibleStates = []
    for row in board:
        for col in range (0, 2):
            if (row[col]) == empty:
                possibleStates.append((board.index(row), col))
    return possibleStates

def result(board, action):
    resultingState = deepcopy(board)
    if board[action[0]][action[1]] == empty:
        if player(board) == 'X':
            resultingState[action[0]][action[1]] = 1
        elif player(board) == 'O':
            resultingState[action[0]][action[1]] = 0
        return resultingState
    else:
        raise Exception('Invalid position. Try again')

def terminal(state):
    countEmpty = 0
    for row in (0, 2):
        for col in (0, 2):
            if state[row][col] == empty:
                countEmpty+=1
    if countEmpty==0:
        return True
    elif win(state):
        return True
    else: 
        return False

def threeInARow(board):
    count_x = 0
    count_y = 0
    for rows in board:
        for i in range(0, 3):
            if rows[i] == 1:
                count_x+=1
                if count_x == 3:
                    return 'X'
            elif rows[i] == 0:
                count_y+=1
                if count_y == 3:
                    return 'Y'
        count_x = 0
        count_y = 0

def threeInAColumn(board):
    count_x = 0
    count_y = 0
    for i in range(0, 3):
        for j in range (0, 3):
            # print('j:', j, 'i:', i)
            if board[j][i] == 1:
                count_x+=1
                if count_x == 3:
                    return 'X'
            elif board[j][i] == 0:
                count_y+=1
                if count_y == 3:
                    return 'O'
        # print(count_x, count_y)
        count_x = 0
        count_y = 0

def diagonalWin(board):
    if board[0][0] == board[1][1] == board[2][2] == 1:
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 0:
        return 'O'
    elif board[2][0] == board[1][1] == board[0][2] == 1:
        return 'X'
    elif board[2][0] == board[1][1] == board[0][2] == 0:
        return 'O'

def win(board):
    if threeInARow(board) == 'X':
        return 'X'
    elif threeInARow(board) == 'O':
        return 'O'
    elif threeInAColumn(board) == 'X':
        return 'X'
    elif threeInAColumn(board) == 'O':
        return 'O'
    elif diagonalWin(board) == 'X':
        return 'X'
    elif diagonalWin(board) == 'O':
        return 'O'

def utility(state):
    outcome = win(state)
    if outcome == 'X':
        return 1
    elif outcome == 'O':
        return -1
    else:
        return 0

def minimax(state):
    states = []
    utilities = []
    if terminal(state):
        # print('here')
        for i in range (0, len(states)):
            u = utility(states[i])
            utilities.append(u)
        return utilities
    else:
        actionsArray = actions(state)
        print(actionsArray)
        for i in range(0, len(actionsArray)):
            if player(state) == 'X':
                nextState = deepcopy(state)
                nextState[actionsArray[i][0]][actionsArray[i][1]] = 1
                states.append(nextState)
            elif player(state) == 'O':
                nextState = deepcopy(state)
                nextState[actionsArray[i][0]][actionsArray[i][1]] = 0
                states.append(nextState)
        print(states)
        actionsArray = []
        # for s in range (0, len(states)):
        #     a = actions(states[s])
        #     actionsArray.append(a)
        print(actionsArray)

        
        # newStates = []
        # for i in range (0, len(states)):
        #     newStates.append(minimax(states[i]))
        # print(newStates, 'newstates')
        # for s in states:
        #     print(states, ': ', s, ': ', minimax(s))


# print(player([[empty, 1, 0], [0, 1, 1], [1, empty, 0]]))
# print(actions([[None, 1, 0], [0, 1, 1], [1, None, 0]]))
# print(result([[None, 1, 0], [0, 1, 1], [1, None, 0]], (0, 0)))
# print(win([[0, 1, 0], [0, 0, 0], [1, 0, 0]]))
# print(win([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
# print(win([[0, 1, 0], [0, 0, 1], [1, 1, 0]]))
# print(utility([[0, 1, 0], [0, 0, 0], [1, 0, 0]]))
# print(utility([[0, 1, 0], [0, 1, 1], [1, 1, 0]]))
# print(utility([[0, 1, 0], [0, 0, 1], [1, 1, 0]]))
print(minimax([[empty, 1, 0], [0, 1, 1], [1, empty, 0]]))