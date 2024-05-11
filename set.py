set1 = {"a","b","c","a"}
set2 = {1,2,3,"a"}
set3 = {"a"}

print(set1.symmetric_difference(set2)) #Ignores if value matches
print(set1)

set1.add("d") #adding a new element in the set
print(set1)

print(set1.union(set2)) #Union of two sets[Returns all unique value]

print(set1.intersection(set2)) #intersection of two sets [Returns only the common value]

set1.update("e") #Update Set-1
print(set1)

print(set1.pop()) #This will Remove any item from the set 

print(set1)

print(set2.issuperset(set3)) #check if set-2 is Superset of set-3

print(set2.issuperset(set3)) #check if set-2 is Subset of set-3

set4 = set1.copy() #Copying set1 to set4

print(set4) 

print(set4.clear()) #Clear all elements from set4

print(set4) #Set4 is now an empty set

 