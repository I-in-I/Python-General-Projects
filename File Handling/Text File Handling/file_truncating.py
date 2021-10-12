#Replaces items in file and truncates to adjust file size

file = open('test.txt', 'r+')


old = input("Enter what to search for: ")
new = input("Enter what to replace with: ")

temp = file.read()
file.seek(0)


temp = temp.replace(old, new)

#Counts new-lines to adjust length
count = temp.count("\n")
length = len(temp) + count

##print(f"TEMP\n{temp}\nEND TEMP")


file.write(temp)

#Truncates file based on length.
file.truncate(length)

file.seek(0)

print(file.read())

file.close()
