## Type your code here
def division(numerator, denominator):
    try:
        result = numerator/ denominator
        return result
    except ZeroDivisionError:
        print("Cannont Divide By Zero.")
        return None
#Inputs
numerator = int(input("Enter the value of Numerator:"))
denominator = int(input("Enter the value of Denominator:"))

print(division(numerator, denominator))