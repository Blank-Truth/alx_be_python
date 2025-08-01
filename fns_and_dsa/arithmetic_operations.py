def perform_operation(num1, num2, operation):
    num1 = float(input("Enter the first number"))
    num2 = float(input("Enter the second number"))
    operation = input("Enter an operation e.g: add, subtract, multiply, divide").strip()
    if operation == "add":
        return num1 + num2 
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide" and num1/num2 != 0:
        return num1 / num2
    else:
        print("invalid operator, try again")