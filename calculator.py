import math_tools 

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

operations = {
    "+" : math_tools.add,
    "-" : math_tools.subtract,
    "*" : math_tools.multiply,
    "/" : math_tools.divide
}

if operation in operations:
    print("Result = ", operations[operation](a, b))
else:
    print("Invalid operation")