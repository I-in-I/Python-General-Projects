from os import strerror
from collections import Counter


try:
    with open(input("Enter file path/name with extension (example.txt): "), "rt") as file:
        file = file.read()
        keys = []
        for char in file:
    ##        print(char)
            file_dict = {char.upper():file.count(char) for char in file if char.isalpha()}

##        for key in file_dict:
##            keys.append(key)
##        sorted_keys = sorted(keys)
        
##        for key in sorted_keys:
##            print(key+":"+str(file_dict[key]))

        with open("frequency.hist", "wt") as hist:
            sorted_count_tuple = Counter(file_dict).most_common()
            
            for key, val in sorted_count_tuple:
                hist.write(key+":"+str(val)+"\n")
                print(key+":"+str(val))
            
            
    ##    print(file)
    ##    print(file_dict)
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
