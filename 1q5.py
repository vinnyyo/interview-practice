# There are three types of edits that can be performed on strings: insert a character, 
# remove a character, or replace a character. Given two strings, write a function to check if they are 
# one edit (or zero edits) away. 

def oneway(string1, string2):
    length = len(string2)
    if len(string1) > len(string2):
        length = len(string1)
    differences = 0
    ind1 = 0
    ind2 = 0
    for i in range(length):
        try:
            if string1[ind1] != string2[ind2]:
                differences += 1
                if ind2 + 1 < len(string2):
                    if string1[ind1] == string2[ind2 + 1]:
                        ind2 += 1
                if ind1 + 1 < len(string1):
                    if string1[ind1 + 1] == string2[ind2]:
                        ind1 += 1
                else:
                    return False
            else:
                ind1 += 1
                ind2 += 1
        except IndexError:
            differences += 1
    if differences > 1:
        return False
    else:
        return True
    
print(oneway("cat","cat"))
print(oneway("at","cat"))
print(oneway("t","cat"))
print(oneway("cat","ca"))
print(oneway("cat","c"))
print(oneway("cat","ct"))
print(oneway("catt","cat"))
print(oneway("cat","cattt"))