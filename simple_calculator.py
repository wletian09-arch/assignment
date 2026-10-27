print("Welcome to Simple Calculator!")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Choose an operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
    print(first_number, "+", second_number, "=", result)

elif operator == "-":
    result = first_number - second_number
    print(first_number, "-", second_number, "=", result)

elif operator == "*":
    result = first_number * second_number
    print(first_number, "*", second_number, "=", result)

elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
        print(first_number, "/", second_number, "=", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operator.")
