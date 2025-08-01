def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    operation = input("Enter an operation i.e: + - * /").strip()
    if operation == "+":
        return num1 + num2 
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("invalid operator, try again")