# Implement a method to perform basic string compression using the counts 
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
# "compressed" string would not become smaller than the original string, your method should return 
# the original string. You can assume the string has only uppercase and lowercase letters (a - z). 

def compress(toCompress):
    matrix = [[toCompress[0], 0]]
    curLttr = 0
    for char in toCompress:
        if matrix[curLttr][0] == char:
            matrix[curLttr][1] += 1
        else:
            matrix.append([char, 1])
            curLttr += 1
    if len(matrix) * 2 >= len(toCompress):
        return toCompress
    output = ""
    for array in matrix:
        output += array[0] + str(array[1])
    return output

print(compress('aabcccccaaa'))