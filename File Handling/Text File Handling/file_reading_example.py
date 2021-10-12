'''
An example of how python reads an iterable file object by default.
invisble \n are shown so the user can see how python delimits new lines
'''

with open('test.txt') as test:
    for line in test:
        if line.endswith('\n'):
            #linedup = line[:-1] + '\\n'
            print(line[:-1] + '\\n')
        else:
            print(line)
