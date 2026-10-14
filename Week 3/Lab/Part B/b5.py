def check_validity(operator: str):
    valid_operators = ["+", "-", "*", "/", "%", ">", ">=", "<", "<="]
    if operator in valid_operators:
        return True
    else:
        return False

def calculate(num1: float, num2: float, operator: str):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
    elif operator == "%":
        return num1 % num2
    elif operator == ">":
        return num1 > num2
    elif operator == ">=":
        return num1 >= num2
    elif operator == "<":
        return num1 < num2
    elif operator == "<=":
        return num1 <= num2

while True:
    try:
        num1 = float(input("First Number: "))
        operator = input("Operator: ")
        num2 = float(input("Second Number: "))

        if not check_validity(operator):
            print("Invalid operator.")

        print(calculate(num1, num2, operator))
    except Exception as e:
        print(f"Error - {e}")
