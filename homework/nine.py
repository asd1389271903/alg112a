# 由chatgpt輔助 已理解
def is_valid_move(maze, x, y):
    # 在移動前確認下一個移動點是否可以前進
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
        return True
    return False

def dfs(maze, x, y, path, visited):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        return path
    
    visited.add((x, y))
    
    #上、下、左、右
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(maze, new_x, new_y) and (new_x, new_y) not in visited:
            # 如果移動是合法的 並且新位置未被訪問過
            new_path = path + [(new_x, new_y)]
            result = dfs(maze, new_x, new_y, new_path, visited)
            if result:
                return result
    
    return None

def solve_maze(maze):
    path = [(0, 0)]
    visited = set()
    result = dfs(maze, 0, 0, path, visited)
    return result

maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

solution = solve_maze(maze)

if solution:
    print("找到路徑:")
    print(solution)
else:
    print("無法找到路徑")
