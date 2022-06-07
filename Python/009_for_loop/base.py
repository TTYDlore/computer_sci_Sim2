lenght = int(input("what do you want the length of the line to be "))
symbol = input("what character do you want the line to be made of ")
direction = input("do you want to have to linebe horizontal ( h ) or vertical ( v ) ")

if direction == "h":
    for x in range(0,lenght):
        print(symbol, end=" ")
elif direction == "v":
    for y in range(0,lenght):
        print(symbol)
else:
    print("input not understood")
print("")