# TLDR for the questions asked:-
# A- A* search is implemented as the search algorithm
# C- Number of states passed: 5435 for two.txt, 6 for one.txt
# B- Steps for Two.txt: 2


def construct_board(file_path):
    board = []
    
    # Open the file for reading
    with open(file_path, 'r') as file:
        for line in file:

            # ^ Splits each line into individual characters (numbers and spaces)

            line = line.strip()  # Remove leading/trailing whitespaces
            row = [int(char) if char != ' ' else 0 for char in line]
            board.append(row)
    
    return board

# Specify the path to your input text file

file_path = "C:/Users/Kavita manoj/Downloads/one.txt" #change as per requirement


gameboard = construct_board(file_path)

# # to check if this works:-

# for row in gameboard:
#     print(row)


import heapq
import copy

# Define the board board
initial_state = gameboard

# hardcoding the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# QA. manhattan distance is the heuristic function and A* search is used

def heuristic(state):
    h = 0 #just for initialisation purposes
    for row in range(3):
        for col in range(3): #iteration over each cell ([row][column] = [i][j])
            if state[row][col] != 0:
                goal_row, goal_col = divmod(state[row][col] - 1, 3)
                h += abs(row - goal_row) + abs(col - goal_col) #manhattan distance = |x1-x0| + |y1-y0|
    return h

# Define a function to find the empty space (0)
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0: #since the space has been converted to 0 by the construct_board function
                return i, j #only returns one value because per board there is only one empty space so the loop does not need to run any further if 0 is encountered

# Define the A* algorithm
def solve_board(initial_state, goal_state):
    open_set = [(0, initial_state)] 
    states = 0 # For Question C
    # because the cost taken from initial_state to initial_state is 0
    closed_set = set() #empty set to track explored states
    
    while open_set: 
        # ^ should keep running until open set is not empty, i.e., breaks when open set becomes empty

        f, current_state = heapq.heappop(open_set) 
        
        # heappop() used to remove and extract the lowest cost f from open_set. 
        # and the state corresponding to lowest cost becomes the current state
        
        if current_state == goal_state:
            return current_state, states  # if the board is goal state/solved
        
        closed_set.add(tuple(map(tuple, current_state)))
        # map(tuple, current_state) converts each row into a tuple
        # tuple of tuple(rows) converts all the rows into a 2-D tuple/nested tuple to make it immutable 
        # the final result is added to the set closed set to mark it as explored

        
        empty_i, empty_j = find_empty(current_state)

        # finds the coordinates of the empty space in the current state (state corresponding to lowest cost)
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = empty_i + di, empty_j + dj 

            # This is akin to moving the empty space (0) to a new position rather than moving tiles to 0
            # (1, 0) moves the 0 DOWN one row, same column
            # (-1, 0) moves the 0 UP one row, same column
            # (0, 1) moves the 0  RIGHT to the next column
            # (0, -1) moves the 0 LEFT to the prev column 


            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = copy.deepcopy(current_state)

                # We dont want to manipulate on the current state to form a new_state so made a deepcopy of the current state to another variable new_state

                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]

                # this exchanges the value of the 0 and the number being swapped with at the position of board[new_i][new_j] where board is new state in this case
        
                
                if tuple(map(tuple, new_state)) not in closed_set:
                    g = f + 1
                    h = heuristic(new_state)
                    heapq.heappush(open_set, (g + h, new_state))
                    steps+=1

                # This block of code adds the new state to closed set if it isn't present in there already
                # f was the minimum cost in the heap queue
                # g is its increment by one because the new state came from a current state by moving the 0 to ONE block
                # h is the manhattan distance from the new state to the goal state
                # heapq.heappush() adds the new state, with a heuristic value of g+h (path cost + manhattan distance to goal state), making it an A* search

    
    return None, states  # if no solution is found despite the loop breaking

"""
Why is a priority queue used using heapq?

- A priority queue is used in this code to efficiently manage and prioritize puzzle states during the A* search algorithm. 
- A priority queue is a data structure that stores elements with associated priorities (as a key value pair, in this case the key was our path cost+manhattan distance to goal (g+h)).
- It thus allows efficient access to and removal of the element with the highest (or lowest) priority. 
- For the above-implemented A* search, the priority queue is used to keep track of puzzle states in a way that allows the algorithm to explore states with lower estimated costs first."""

# Solve the board
solution = solve_board(initial_state, goal_state)

# Print the solution
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")