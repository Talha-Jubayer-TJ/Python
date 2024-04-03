greet = "***Welcome to The Calculator App***"
print(greet.center(50))
name = input("Please Enter your name first: ")
print("Welcome!", name, ":-)")

num1 = float (input("Enter First Number: "))
num2 = float (input("Enter Second Number: "))
operator = input("Enter a Operator: ")


if operator == "+":
    print("Addtion of ", num1,operator,num2, "is: ", num1 + num2)
elif operator == "-":
    print("Substraction of ", num1, operator ,num2, "is: ", num1 - num2)
elif operator == "*":
    print("Multiplication of ", num1,operator,num2, "is: ", num1 * num2)
elif operator == "/":
    print("Division of ", num1,operator,num2, "is: ", num1 / num2)
elif operator == "%":
    print("Reminder of ", num1,operator,num2, "is: ", num1 % num2)
else:
    print("Enter a valid 'Operator'")