num = int(input("Enter Your Number: "))
match num:
    case 0:
        print("Entered Number is Zero.")
    case 7:
        print("Entered Number is Seven.")
    case 13:
        print("Entered Number is Thirteen.")
    case _ if num < 0:
        print("Entered Number is Negative.")
    case _ if num > 0:
        print("Entered Number is ", num)
    case _ if num > 100:
        print("Entered Number is greater than 100")
