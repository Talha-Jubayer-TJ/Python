greet = "Welcome to 'Kaun banega Corerpati' "

questions = [
    ["What is the capital of Bangladesh?", "Dhaka", "Khulna", "Cumilla", "Jassore", 1],
    ["What is the National Animal of Bangladesh?", "Cat", "Tiger", "Lion", "Dog", 2],
    ["What is the National Flower of Bangladesh?", "Rose", "Orchid", "Tulip", "Water Lily", 4],
    ["What is the capital of Bangladesh?", "Dhaka", "Khulna", "Cumilla", "Jassore", 3],
    ["What is the capital of Bangladesh?", "Dhaka", "Khulna", "Cumilla", "Jassore", 3],
]

levels = [1000, 2000, 3000, 4000, 5000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestions for: {levels[i]} Tk")
    print(f"# {questions[i][0]} ")
    print(f"a. {questions[i][1]}         b. {questions[i][2]}")
    print(f"c. {questions[i][3]}         d. {questions[i][4]}")
    
    result = input('Enter your result between (1-4) / Press 0 to Quit: ')

    if result == '0':
        print(f"You have decided to quit. You will take {money} Tk with you.")
        break

    result = int(result)

    if result == question[-1]:
        print(f"Correct Answer! You have won {levels[i]} Tk")
        money += levels[i]
        if i in [4, 9, 12, 15]:
            print(f"You have reached a milestone! You will take {money} Tk with you.")
    else:
        print("Wrong Answer! Try Again Later! :(")
        print(f"You will take {money} Tk with you.")
        break

if i == len(questions) - 1:
    print("Congratulations!! You have answered all questions correctly!")
    print(f"You will take {money} Tk with you.")
