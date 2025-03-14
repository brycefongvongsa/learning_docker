import math

def performOperation(*args, operation=None):
    if operation == 'add':
        return sum(args)
    elif operation == 'subtract':
        return subtract(args)
    elif operation == 'multiply':
        return multiply(args)
    elif operation == 'divide':
        return divide(args)
    else:
        return "Invalid operation"

def subtract(args):
    result = args[0]
    for i in range(1, len(args)):
        result -= args[i]
    return result

def multiply(args):
    result = args[0]
    for i in range(1, len(args)):
        result *= args[i]
    return result

def divide(args):
    result = args[0]
    for i in range(1, len(args)):
        result /= args[i]
    return result
