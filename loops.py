names = ['Talha',  'Mahadi', 'Abid', 'Nabik', 'Adil']
for index, name in enumerate(names):
    print(f"At position {index}, I found a {name}")
    
print("Printing a List.")
for name in names:
    print(name, end='-')
    for alpha in name:
        print(alpha, end=",")

print("\nPrinting a range of EVEN Numbers")
for num in range(0, 50, 2):
    print( num , end=" ")

print("\nPrinting a range of ODD Numbers")
for num in range(0, 50, 2):
    print( num+1 , end=" ")