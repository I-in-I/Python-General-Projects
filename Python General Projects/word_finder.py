#word_finder searches for a string inside another string,
#from left to right only, and continuing from the next index
#of the last elemnt found


word = input("Enter word to search for: ").upper()
letters = input("Enter letters to search in: ").upper()


found = True
index = 0

#searches for each element in the inputed word
for char in word:
    
    #checks for element found (-1 returned if not found)
    if letters.find(char, index) > -1:
        
        #gets index of current iteration
        index = letters.index(char)
        index += 1
    else:
        found = False


if found == True:
    print("Word Found")
else:
    print("Word Not Found")
