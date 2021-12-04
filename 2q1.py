# Write code to remove duplicates from an unsorted linked list. 
# FOLLOW UP 
# How would you solve this problem if a temporary buffer is not allowed?

def noDuplicates(linkedList):
    return remove(0, linkedList)

def remove(indexAfter, linkList):
    index = indexAfter + 1
    while index < len(linkList):
        if linkList[indexAfter] == linkList[index]:
            del linkList[index]
        else:
            index += 1
    if indexAfter <= len(linkList):
        return remove(indexAfter + 1, linkList)
    else:
        return linkList

print(noDuplicates([1,5,66,3,7,5,8]))
print(noDuplicates([1,5,66,3,3,7,5,8,8,3]))