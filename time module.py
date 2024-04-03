from time import strftime
# timestamp = strftime('%H:%M:%S') #Time in Hour Minute Second 
timestamp = int(strftime('%H')) #Only Hour

if (timestamp > 6) and (timestamp < 12) :
    print("Good Morning. Have a Good Day!")
elif (timestamp > 12) and (timestamp < 18):
    print('Good Afternoon!')
elif (timestamp > 18) and (timestamp < 20):
    print("Good Evening")
else:
    print("Good Night, Sweet Dreams.")