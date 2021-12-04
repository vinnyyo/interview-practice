# Given two strings, write a method to decide if one is a permutation of the 
# other.

def isPermutation(string1, string2):
    table1 = {}
    table2 = {}
    for character in string1:
        if character not in table1.keys():
            table1[character] = 1
        else:
            table1[character] += 1
    for character in string2:
        if character not in table2.keys():
            table2[character] = 1
        else:
            table2[character] += 1
    if len(table1.keys()) != len(table2.keys()):
        return False
    for key in table1.keys():
        if key not in table2.keys():
            return False
        if table1[key] != table2[key]:
            return False
    return True

print(isPermutation("dgdhiopppppp", "gehl"))
print(isPermutation("gary", "yarg"))
print(isPermutation("gary", "yarp"))