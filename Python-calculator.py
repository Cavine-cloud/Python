operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
  result = num1 + num2
  print(result)
elif operator == "-":
  result = num1 - num2
  print(result)
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  result = num1 / num2
  print(result)