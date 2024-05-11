num = int(input("Enter a Number to find it's Factorial:"))

def factorial(num):
    if (num==1 or num==0):
        return 1
    else:
        return num * factorial(num-1)

print(f"Factorial of {num} is:",factorial(num))