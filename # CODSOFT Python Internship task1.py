# CODSOFT Python Internship
# Task 1 - Simple Calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("=== Simple Calculator ===")
print("Operations: +  -  *  /")

while True:
    choice = input("\nEnter operation (+, -, *, /) or 'exit' to quit: ").strip()

    if choice.lower() == 'exit':
        print("Goodbye!")
        break

    if choice not in ['+', '-', '*', '/']:
        print("Invalid operation, try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = sub(num1, num2)
    elif choice == '*':
        result = mul(num1, num2)
    elif choice == '/':
        result = div(num1, num2)

    print("Result =", result)