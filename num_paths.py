def numPaths(gridSize):
    grid = [[0 for i in range(gridSize + 1)] for j in range(gridSize + 1)]

    for i in range(gridSize):
        grid[i][gridSize] = 1
        grid[gridSize][i] = 1

    for i in range(gridSize - 1, -1, -1):
        for j in range(gridSize - 1, -1, -1):
            grid[i][j] = grid[i + 1][j] + grid[i][j + 1]

    return grid[0][0]

print(numPaths(2))
print(numPaths(20))
