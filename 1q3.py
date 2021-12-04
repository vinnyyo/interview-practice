# Write a method to replace all spaces in a string with '%20'. You may assume that the string 
# has sufficient space at the end to hold the additional characters, and that you are given the "true" 
# length of the string. (Note: If implementing in Java, please use a character array so that you can 
# perform this operation in place.) 

def urlify(input):
    output = ""
    for character in input.strip():
        if character == " ":
            output += "%20"
        else:
            output += character
    return output

print(urlify("Mr john bon jovy"))
