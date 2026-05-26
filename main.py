calc1 = float(input("What is your first number?"))
calc2 = float(input("What is your second number?"))
arithmetic = float(input("1 for add, 2 for minus, 3 for multiply, 4 for divide"))


def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

if arithmetic == 1:
    print(add(calc1,calc2))

if arithmetic == 2:
    print(subtract(calc1,calc2))

if arithmetic == 3:
    print(multiply(calc1,calc2))

if arithmetic == 4:
    print(divide(calc1,calc2))

