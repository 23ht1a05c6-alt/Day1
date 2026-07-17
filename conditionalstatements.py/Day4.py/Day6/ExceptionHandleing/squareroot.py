import math

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Negative number")
    print("Square Root:", math.sqrt(num))
except ValueError:
    print("Error: Enter a positive number.")