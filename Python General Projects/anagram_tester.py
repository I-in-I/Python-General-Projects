#input
potential_anagram_input1 = input("Enter First Text: ")
potential_anagram_input2 = input("Enter Second Text: ")

#convert input to uppercase
upper_case_anagram1 = potential_anagram_input1.upper()
upper_case_anagram2 = potential_anagram_input2.upper()

#store input in list
potential_anagram_list1 = upper_case_anagram1.split()
potential_anagram_list2 = upper_case_anagram2.split()

#join list2 into joined
potential_anagram_joined1 = ''.join(potential_anagram_list1)
potential_anagram_joined2 = ''.join(potential_anagram_list2)

#sort joined strings
potential_anagram_sorted1 = sorted(potential_anagram_joined1)
potential_anagram_sorted2 = sorted(potential_anagram_joined2)

#print true/false on result of comparing joined and reversed
if potential_anagram_sorted1 == potential_anagram_sorted2:
    print("This is an anagram. TRUE")
else:
    print("This is not an anagram. FALSE")
    
