# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome 
# is a word or phrase that is the same forwards and backwards. A permutation 
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palinperm(input):
    letterCount = {}
    for char in input.strip().lower():
        if char != " ":
            if char in letterCount.keys():
                letterCount[char] += 1
            else:
                letterCount[char] = 1
    oddCount = 0
    for char in letterCount.keys():
        if letterCount[char] % 2 == 1:
            oddCount += 1
    if oddCount == 1 or oddCount == 0:
        return True
    else:
        return False

print(palinperm("taco cat"))
print(palinperm("Taco cat"))
print(palinperm("taco cab"))
print(palinperm("racecar"))
print(palinperm("toot"))