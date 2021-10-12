#input
potential_palindrome_input = input("Enter Text: ")

#convert input to uppercase
upper_case_palindrome = potential_palindrome_input.upper()

#store input in list
potential_palindrome_list = upper_case_palindrome.split()

#create copy of list into list2
potential_palindrome_list2 = potential_palindrome_list[:]

#join list2 into joined
potential_palindrome_joined = ''.join(potential_palindrome_list2)

#reverse joined
potential_palindrome_reversed = potential_palindrome_joined[::-1]

#print true/false on result of comparing joined and reversed
if potential_palindrome_joined == potential_palindrome_reversed:
    print("This is a palindrome. TRUE")
else:
    print("This is not a plaindrome. FALSE")
    
