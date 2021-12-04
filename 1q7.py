# Given an image represented by an NxN matrix, where each pixel in the image is 4 
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate(matrix):
    n = len(matrix)
    output = [ [ 0 for i in range(n) ] for j in range(n) ]
    for numby in range(n):
        for numbx in range(n):
            output[numbx][n - 1 - numby] = matrix[numby][numbx]
    return output

def rotateInPlace(matrix):
    return None



'''
00-02 [x][n-y]
01-12
02-22

10-01
11-11
12-21

20-00
21-10
22-20
'''

'''
in place 
02 temp var
00-02 [x][n-y]
20-00
22-20
02-22

12 temp
01-12
10-01
21-10
12-21
'''

print(rotate([
    [1, 0, 0],
    [0, 0, 1],
    [1, 0, 0]]))
print(rotate([
    [1, 0, 0, 7],
    [0, 0, 1, 7],
    [1, 0, 0, 4],
    [4, 222, 35, 7]]))