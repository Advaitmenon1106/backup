import heapq
import copy

# Define the puzzle board
initial_state = [
    [6, 8, 1],
    [4, 7, 3],
    [5, 0, 2]
]

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Define the heuristic function (Manhattan distance)
def heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                h += abs(i - goal_row) + abs(j - goal_col)
    return h

# Define a function to find the empty space (0)
def find_empty(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Define the A* algorithm
def solve_puzzle(initial_state, goal_state):
    open_set = [(0, initial_state)]
    closed_set = set()
    
    while open_set:
        f, current_state = heapq.heappop(open_set) # heappop() used to remove and extract the lowest value from open_set. 
        #open_set 
        
        if current_state == goal_state:
            return current_state  # Puzzle is solved
        
        closed_set.add(tuple(map(tuple, current_state)))
        
        empty_i, empty_j = find_empty(current_state)
        
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i, new_j = empty_i + di, empty_j + dj
            
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = copy.deepcopy(current_state)
                new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
                
                if tuple(map(tuple, new_state)) not in closed_set:
                    g = f + 1
                    h = heuristic(new_state)
                    heapq.heappush(open_set, (g + h, new_state))
    
    return None  # No solution found

# Solve the puzzle
solution = solve_puzzle(initial_state, goal_state)

# Print the solution
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
