def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2
    
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Which operation do you want to carry out? Type out the symbol.: ")
        num2 = float(input("What is the next number?: "))
        calc_function = operations[operation_symbol] 
        answer = calc_function(n1=num1, n2=num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type \'y\' to continue calculating with {answer}, or type \'n\' to exit.: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


