symbol = input("what do you want the box to made of ")
width = int(input("What do you want the width of the box to be "))
hight = int(input("What do you want the hight of the box to be"))
for x in range(0,hight):
    print("")
    for y in range(0,width):
        print(symbol, end="")
print("")