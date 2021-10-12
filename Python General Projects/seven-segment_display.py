def make_list_of_string_digits(input_string):
    string_list = []
    for ch in input_string:
        string_list.append(ch)
    return string_list


def convert_string_list_to_segments(string_list):
    for item in string_list:
        display_number(item)


L1 = []
L2 = []
L3 = []
L4 = []
L5 = []


def display_number(input_string):
    if input_string == '1':
        L1.append('# ')
        L2.append('# ')
        L3.append('# ')
        L4.append('# ')
        L5.append('# ')
    elif input_string == '2':
        L1.append('### ')
        L2.append('  # ')
        L3.append('### ')
        L4.append('#   ')
        L5.append('### ')
    elif input_string == '3':
        L1.append('### ')
        L2.append('  # ')
        L3.append('### ')
        L4.append('  # ')
        L5.append('### ')
    elif input_string == '4':
        L1.append('# # ')
        L2.append('# # ')
        L3.append('### ')
        L4.append('  # ')
        L5.append('  # ')
    elif input_string == '5':
        L1.append('### ')
        L2.append('#   ')
        L3.append('### ')
        L4.append('  # ')
        L5.append('### ')
    elif input_string == '6':
        L1.append('### ')
        L2.append('#   ')
        L3.append('### ')
        L4.append('# # ')
        L5.append('### ')
    elif input_string == '7':
        L1.append('### ')
        L2.append('  # ')
        L3.append('  # ')
        L4.append('  # ')
        L5.append('  # ')
    elif input_string == '8':
        L1.append('### ')
        L2.append('# # ')
        L3.append('### ')
        L4.append('# # ')
        L5.append('### ')
    elif input_string == '9':
        L1.append('### ')
        L2.append('# # ')
        L3.append('### ')
        L4.append('  # ')
        L5.append('### ')
    elif input_string == '0':
        L1.append('### ')
        L2.append('# # ')
        L3.append('# # ')
        L4.append('# # ')
        L5.append('### ')
    else:
        print('Invalid Character: ' + input_string)


def print_segments():
    for item in L1:
        print(item, end='')
    print()
    for item in L2:
        print(item, end='')
    print()    
    for item in L3:
        print(item, end='')
    print()    
    for item in L4:
        print(item, end='')
    print()    
    for item in L5:
        print(item, end='')    
    print()


input_string = input('Enter number: ')

string_list = make_list_of_string_digits(input_string)

convert_string_list_to_segments(string_list)

print_segments()
