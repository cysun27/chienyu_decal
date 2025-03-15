def add(a, b):
    """add the two input values"""
    return a + b

def subtract(a, b):
    """subtract the second input value from the first input value"""
    return a - b

def multiply(a, b):
    """multiply the two input values"""
    return a*b

def divide(a, b):
    """divide the first input value by the second input value, except when the second input value is zero"""
    if b == 0:
        return("Undefined")
    else:
        return a/b