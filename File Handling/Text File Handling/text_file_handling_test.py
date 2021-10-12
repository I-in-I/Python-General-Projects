from os import strerror

try:
   with open('test.txt', 'w+') as fo:
        for i in range(10):
            fo.write("line #" + str(i+1) + "\n")
        fo.seek(0)
        s = fo.read()
        print(s)
        
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
