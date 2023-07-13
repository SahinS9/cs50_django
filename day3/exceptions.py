# x = int(input("x : "))
# y = int(input("y : "))

# print( f" x/y is {x/y}")

# result = x/y
# print(f"{x}/{y} = {result}")

# if y will be zero, need to run away from error
import sys
try:
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError:
    print("Error: Input is not numeric")
    sys.exit(1)
    #status code 1 is means: Something went wrong

try:
    result = x/y
except ZeroDivisionError:
    print("error: Cannot divide by 0.")
    sys.exit(1)
    #status code 1 is means: Something went wrong
print(result)
