names = ['Talha',  'Mahadi', 'Abid', 'Nabik', 'Adil']

i = 0

new = []

while i < len(names):
    j = names[i]
    
    if (len(j) >= 4):
        new.append(j)
    
    # print(j) 
    i = i + 1
print(new)