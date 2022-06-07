import random
randlist = []
amount = int(input("how many random numbers would you want "))
y = 0
for i in range (0,amount):
    y = (random.randrange(0,10))
    randlist.append(y)
for E in range (0,amount):
    print(randlist[E], end=", ")
print(randlist)
