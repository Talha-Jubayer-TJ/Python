def sum(a, operator, b ):
    """_summary_

    Args:
        a (_type_): _description_
        operator (_type_): _description_
        b (_type_): _description_

    Returns:
        _type_: _description_
    """
    if operator == "+":
        value = a + b
    elif operator  == "-":
        value = a - b
    elif operator == "*":
        value = a * b
    elif operator == "/":
        value = a / b
    else:
        print("Enter a valid Operator.")
    return value

num1 = int (input("Enter a num:") )
num2 = int (input("Enter another num:") )
operator = input("Enter a Operator: ")

print(num1, operator, num2, "is ", sum(num1, operator, num2 ))


