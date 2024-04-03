user_choice = 1
if user_choice == 1:
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        print("Collect Your amount of:", amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")
