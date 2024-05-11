names = ['Talha',  'Mahadi', 'Abid', 'Nabik', 'Adil']
i = 0
new = []
while i < len(names):
    j = names[i] #storing each value of names
    if (len(j) >= 4): #matching the value of string
        new.append(j)
    # print(j) 
    i = i + 1
print(new)