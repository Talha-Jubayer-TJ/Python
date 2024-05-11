num = int(input("Enter a Number to find it's fibonacci series:"))

def fib(num):
    if (num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        return  fib(num-1) + fib (num-2)

print(fib(num))

# fib 4 +fib 3
# fib 2 + fib 1
# fib 1