import math

def sqrt(number):
    try:
        result = math.sqrt(number)
        print(f"Square root of Given number is:{result} ");
    except ValueError:
        print("Please Enter a Positive Integer or Float Value.")

number = float(input("Enter a Number to finds it Square Root:"))
print(sqrt(number))
