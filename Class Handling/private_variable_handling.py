#This shows how to access private instance (through name mangling)
#and class attributes.

class A:
    __x = 1
    def __init__(self):
        self.__var = 10
 
    def get_var(self):
        return self.__var



a = A()


#Printing the returned value of (private) __var from the
#"get" function in class A.
print(a.get_var())


#Printing the value of the (private) class variable __x
print(A._A__x)


#Accessing and assigning/overwriting a value to the (private) __var in
#instance "a".
a._A__var = 100

#Printing the aforementioned instace __var from "a" directly,
#without a function, and showing the value has changed from 10 to 100.
print(a._A__var)


#An example showing that this "a.__var" assignment actually creates
#an (not private) instance variable named "__var" in object "a" which is not
#not related to the private, instanced, __var in object "a".
a.__var = 5
print(a.get_var())


