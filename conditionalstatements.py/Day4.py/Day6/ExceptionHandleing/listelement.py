try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Enter index: "))
    print("Element:", numbers[index])
except IndexError:
    print("Error: Invalid index.")
except ValueError:
    print("Error: Enter a valid number.")