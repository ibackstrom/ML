import math

maze = [
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 3, 0, 1, 1, 0, 1]
]

def find_start_end(maze):
    start = None
    end = None 
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col==3:
                start=(i,j)
            if col==2:
                end=(i,j)
    return start, end

def is_valid_move(maze, visited, row, col):
    rows=len(maze)
    cols = len(maze[0])

    if(0 <= row < rows) and (0 <= col <cols) and maze[row][col] != 1 and not visited[row][col]:
        return True
    return False

def solve_maze(maze, start, end):
    directions = [(-1,0),
                  (0,1),
                  (1,0),
                  (0,-1)]
    paths = []
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))] 
    
    def dfs(row, col):
        if (row,col) == end:
            paths.append((row, col))
            return True
        if is_valid_move(maze, visited, row,col):
            visited[row][col]=True
            paths.append((row,col))

            for x, y in directions:
                if dfs(row+x, col+y):
                    return True
            paths.pop()

        return False 
    start_row, start_col = start
    dfs(start_row,start_col)
    return paths 

start, end = find_start_end(maze)
solution_paths = solve_maze(maze,start,end)

print(solution_paths)






