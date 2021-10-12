#Shows that a class' constructor can be called directly (outside the class).

#Classes have a __new__ method is responsible for creating and returning a new
#instance of your class.

#The __init__ function doesn't return anything and is only responsible for
#initializing the instance.

class Foo:
    def __init__(self, s):
        self.s = s

o = Foo('abc')
print(o.s)

Foo.__init__(o, 'xzy')
print(o.s)
