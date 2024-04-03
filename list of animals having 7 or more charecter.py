Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
new = []
i = 0

while i < len(Animals):
    j = Animals[i];
    if (len(j) == 7):
        new.append(j)
    i = i +1
print(new)
