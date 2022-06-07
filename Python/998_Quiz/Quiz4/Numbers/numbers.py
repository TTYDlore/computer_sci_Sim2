import random
numlist = []
size = int(input("How many numbers do you want in your list "))
e = 0
for i in range(0,size):
    e = random.randrange(-100,200)
    numlist.append(e)
print("Your list is " + str(numlist))
small = numlist[0]
for z in numlist:
    if z < small:
        small = z
BIG = numlist[0]
for A in numlist:
    if A > BIG:
        BIG = A
mid = 0
for m in numlist:
    mid = mid + m
mid = mid / size
print("Your smalest number is " + str(small))
print("Your Bigest number is " + str(BIG))
print("Your average number is " + str(mid))