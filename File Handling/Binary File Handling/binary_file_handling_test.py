from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    with open('file.bin', 'wb+') as bf:
        bf.write(data)
        bf.seek(0)
        rf = bf.read()
        for i in rf:
            print(i)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.

data = bytearray(100)

##for i in range(len(data)):
##    data[i] = 10 + i

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
