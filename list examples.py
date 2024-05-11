list = [4,5,6,7,78,8,9,9,10]
print (list) 
print(list[4:len(list)])
print(list[:len(list)-4])

#Generating List with for loop

#Even Numbers in range of 100
list = [item for item in range(100) if item%2 == 0]
print(list)

names = ["Akash", "Samia", "Nupur", "Nabik", "Kamal", "Rasel", "Rakib", "Sanjida", "Shopnil"]

name_having_four_char = [item for item in names if(len(item) > 5)]
print(name_having_four_char)

name_having_char_R = [item for item in names if "R" in item]
print(name_having_char_R)

# List Manipulation
l = [1.3,4,6,7,8,94,3,54,65,7,8,453,3,454,65657,68,6,8,8,7]

print ("Printing List",l)
l.sort()
print("Sorted List",l)
print("Index of 454 is -",l.index(454))

l.reverse()
print("Reverse List",l)
l.append(9)
print("Adding 9 in List",l)

print("Number of 8 in List",l.count(8))

m = l.copy()

print("Printing m ->", m)
m[0] = 2

print(m)

m.insert(2, 4)
print("adding 4 in index 2",m)


a = [1,2,3,4,5]
print("Printing a - ",a)

b = [9,8,7,6]
print("Printing b -",b)

c = a + b

print("Concatanating a and b",c)

d = [13,14,25]
d.extend(a)
print("Extend a in d", d)


