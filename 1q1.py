# Implement an algorithm to determine if a string has all unique characters. What if you 
# cannot use additional data structures?

def uniqueChars(string):
    hashtable = {}
    for character in string:
        if character in hashtable.keys():
            return False
        hashtable[character] = True
    #print(hashtable)
    return True

catput = "avfbekh"
dogput = "ahrpivskjh"
print(uniqueChars(catput))
print(uniqueChars(dogput))