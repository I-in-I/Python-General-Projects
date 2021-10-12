def mysplit(string):
# A replica of Python's built-in split method
    
    current_word = ''
    final_list = []

         
    for ch in string:
        # Concatenates any chararcter that is not white space
        # into current_word
        if ch not in [' ', '\n', '\t']:
            current_word += ch
        else:
            # If word is not empty, add to list and reset word to empty
            if current_word != '':
                final_list.append(current_word)
                current_word = ''

    # If we reach the end of a string with a word inside curernt_word
    # append that word to final_list and return the list
    if current_word != '':
        final_list.append(current_word)
        
    return final_list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
