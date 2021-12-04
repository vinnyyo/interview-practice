# Assume you have a method isSubstring which checks if oneword is a substring 
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one 
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def isSubstring(sub, string):
    return sub in string

def isRotation(s1, s2):
    curString = s1
    for i in range(len(s1)):
        if curString == s2:
            return True
        else:
            curString = curString[-1] + curString[0:-1]
    return False

print(isRotation("candle", "bat"))
print(isRotation("erbottlewat", "waterbottle"))