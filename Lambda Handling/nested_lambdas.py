# Python program to demonstrate
# nested lambda functions


square = lambda x: x**2
product = (lambda f, n: (lambda x: f(x)*n))

ans = product(square, 2)(10)
print(ans)
