def perform_operation ():
    num1=(float)(input("Enter the first number: "))
    num2=(float (input("Enter the second number:")))
    operation=((input("Enter the operation (add, subtract, multiply, divide):")))
    if operation == 'add':
        print("Result: ", num1 + num2)
    elif operation == 'subtract':
        print("Result: ", num1 - num2)
    elif operation == 'multiply':
        print("Result: ", num1 * num2)
    elif operation == 'divide':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print("Result: ", num1 / num2)
    else:
        print("Error: Invalid operation")

perform_operation()