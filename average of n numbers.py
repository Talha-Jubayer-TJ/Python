def average (*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

average(2,3,4,5,56,66)
