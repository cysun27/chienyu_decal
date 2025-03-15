import math_tools 

operations = {
    "+" : math_tools.add,
    "-" : math_tools.subtract,
    "*" : math_tools.multiply,
    "/" : math_tools.divide
}


def do_operation(a, b, operation):
    if operation in operations:
        print("Result:", operations[operation](a, b))
    else:
        print("Invalid operation")


def calc_init():
    print("Welcome to the simple calculator!")
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    do_operation(a, b, operation)
    log_calc(a, b, operation)


def calc_cont():
    while True:
        a = input("Enter the first number (or 'q' to quit): ")
        if a == "q":
            print("Goodbye!")
            break
        else:
            a = float(a)
        b = input("Enter the second number (or 'q' to quit): ")
        if b == "q":
            print("Goodbye!")
            break
        else:
            b = float(b)
        operation = input("Choose an operation (+, -, *, /) (or 'q' to quit): ")
        if operation == "q":
            print("Goodbye!")
            break
        else:
            do_operation(a, b, operation)
            log_calc(a, b, operation)


def log_calc(a, b, operation):
    file = open("calc_history.txt","a")
    calculation = str(a) + " " + operation + " " + str(b) + " = " + str(operations[operation](a, b)) + "\n"
    file.write(calculation)


calc_init()
calc_cont()