num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()  
else:
    print("Invalid operation. Please enter +, -, *, or /.")
    exit() 

if result.is_integer():
    print(f"{num1} {operation} {num2} = {int(result)}")  
     
