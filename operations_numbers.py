num1 = int(input())
num2 = int(input())
operator = input()

result = 0

if num2 == 0:
    print(f"Cannot divide {num1} by zero")

elif operator == "+":
    result = f"{num1} + {num2} = {num1 + num2}" + (" - even" if (num1 + num2) % 2 == 0 else " - odd")
    print(result)

elif operator == "-":
    result = f"{num1} - {num2} = {num1 - num2}" + (" - even" if (num1 - num2) % 2 == 0 else " - odd")
    print(result)

elif operator == "*":
    result = f"{num1} * {num2} = {num1 * num2}" + (" - even" if (num1 * num2) % 2 == 0 else " - odd")
    print(result)

elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result:.2f}")

elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
