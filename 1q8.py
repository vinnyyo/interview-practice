# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and 
# column are set to 0.

def bomberman(matrix):
    m = len(matrix)
    n = len(matrix[0])
    targets = []
    for row in range(m):
        for num in range(n):
            if matrix[row][num] == 0:
                targets.append([row, num])
    for target in targets:
        for row in range(m):
            matrix[row][target[1]] = 0
        for col in range(n):
            matrix[target[0]][col] = 0
    return matrix

print(bomberman([
    [1,1,1,1,1],
    [1,1,1,0,1],
    [1,1,1,1,1],
    [2,1,1,2,1]
]))
