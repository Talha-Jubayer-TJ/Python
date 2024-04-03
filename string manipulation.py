print("Welcome to the Console".center(50))

while True:
    string_input = input("Enter a String of more than 5 letters: ")
    
    if len(string_input) > 5:
        print("Length of given String is:", len(string_input))
        print("Splitting the String:", string_input.split())
        print("Making the String as Title:\n", string_input.title())
        print("Is the String in Title:", string_input.istitle())

        print("Slicing the String:", string_input[0:7])
        print("Slicing the String with negative indexing:", string_input[-7:])

        print("Replacing a word in String:", string_input.replace("Console", "Terminal"))

        print("Finding the index of the word 'to' in the String:", string_input.find("to"))

        print("Number of letter 't' in the String is:", string_input.count("t"))

        print("Lower case of the String:", string_input.lower())

        print("Upper case of the String:", string_input.upper())

        print("Using for loop for printing the String.")
        for char in string_input:
            print(char)
        break  # Exit the loop once a valid input is entered
    else:
        print("Entered String is less than the limit. Please try again.")
