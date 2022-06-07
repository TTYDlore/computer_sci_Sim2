shoping_list = []
price_list = []
amount = int(input("how many items will you like to buy"))
for i in range (0,amount):
    x = (input("what item would you like to buy "))
    shoping_list.append(x)
    y = float(input("how much does the " + str(x) + " cost? "))
    price_list.append(y)
    print("Thank you for buying " + str(x))
    
total = 0
for t in range(0,amount):
    total = total + price_list[t]

print("here is your receipt ")
for r in range(0,amount):
    print(shoping_list[r] + " - " + str(price_list[r]))
print("totat - " + str(total) )