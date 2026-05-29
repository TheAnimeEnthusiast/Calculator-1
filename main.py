try:
    calc1 = float(input("What is your first number? "))
    calc2 = float(input("What is your second number? "))
    arithmetic = int(input("1 for add, 2 for minus, 3 for multiply, 4 for divide: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

if arithmetic == 1:
    print(add(calc1, calc2))
elif arithmetic == 2:
    print(subtract(calc1, calc2))
elif arithmetic == 3:
    print(multiply(calc1, calc2))
elif arithmetic == 4:
    print(divide(calc1, calc2))
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
