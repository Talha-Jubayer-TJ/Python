print("Welcome to the Console".center(50))
str = input("Enter a String of more than 10 letter: ")

# while len(str) < 10 :
#     input("Enter a String of more than 10 letter : ")  

if len(str) > 10:
    print("Length of given String is : ",len(str))

    print("Spliting the String",str.split())
    print("Making the String as Title\n",str.title())

    print("Is the String in Title :",str.istitle())

    print("Slicing the String:", str[0:7])

    print("Slicing the String with negative indexing:", str[-7:])

    print("Replacing a word in String:", str.replace("Console", "Terminal"))

    print("Finding the index of word 'to' in the String:", str.find("to"))

    print("Number of letter 't' in the String is:", str.count("t"))

    print("Lower case of the String:", str.lower())

    print("Upper case of the String:", str.upper())

    print("Using for loop for printing the String.")
    for char in str:
        print(char)
else:
    print("Entered String is less than the limit")
