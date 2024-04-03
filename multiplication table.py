print("Multipication Tables Of Given Number". center(50))

num = int(input("Enter a number to get it's Multiplication Table: "))

if num > 0:
    for item in range(1,11):
        print(num, "*", item, "=", num * item)
else:
    print("Enter a Positive Integer Number.")