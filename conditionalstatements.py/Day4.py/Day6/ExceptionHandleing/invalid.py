try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Invalid input. Enter a number")