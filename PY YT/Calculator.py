def floordivision(a,b):
    if b>0:
        return a//b
    else:
        print("Error: Division by zero is not allowed.")
def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b>0:
        return a/b
    else:
        print("Error: Division by zero is not allowed.")
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
print("Sum:",sum(a,b))
print("Subtract:",subtract(a,b))
print("Multiply:",multiply(a,b))
print("Divide:",divide(a,b))
print("Floordivision:",floordivision(a,b))
