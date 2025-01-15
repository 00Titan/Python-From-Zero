def calculation(a, sign, b):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    else:
        print("Error: Invalid operation!")

def main():
    while True:
        a = input(f"Enter the first number (or exit to quit): ")
        if a.lower() == "exit":
            print("Program terminated.")
            break

        try:
            a = int(a)
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        sign = input("Enter the operation (+, -, *, /): ")
        if sign not in {"+", "*", "-", "/"}:
            print("Error: Invalid operation! Please use +, -, *, or /.")
            continue

        b = input(f"Enter the second number: ")
        try:
            b = int(b)
        except ValueError:
            print("Error: Please enter a valid number!")
            continue

        result = calculation(a, sign, b)
        print(f"The result is {result}.\n")
main()