#This block shows the structure of a try-except block with "else" and "finally"
#mixed in. the order must be:
#try>specific exceptions>only one general exception>
#else after all exceptions>finally last.

#"finally" requires a "try" statement to work.

#"else" treats exceptions as "if" statements, only executing when the preceding
#exceptions do not execute, and "finally" always executes.

try:
    print(1/1)
except ZeroDivisionError:
    print("ZDE")
except TypeError:
    print("Type")
except:
    print('general')
else:
    print("else")
finally:
    print('final')


#This block shows "finally" executes even when a break is used before it.

while True:
    try:
        print(1/0)
    except:
        print('general')
        break
    finally:
        print('final')


#This block shows how "break" stops else from executing by cancelling the
#while loop (which is seen as an "if" statement by the else) even if else
#is outside the loop.

flag = True
while flag:
    print(1/1)
    flag = False
    break
else:
    print('else')
