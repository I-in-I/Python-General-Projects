class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value


class Stack_sum(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        Stack.push(self, val)
        self.__sum += val

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val


        
my_stack = Stack_sum()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.get_sum())


for i in range(3):
    var = my_stack.pop()
##    print(var)        

print(my_stack.get_sum())

