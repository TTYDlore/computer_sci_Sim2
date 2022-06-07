import random
restaurant_list = ["subway (0)", "scarantinos(1)","Monster Sushi(2)"]
subway_list = ["subway culb", "Baja turkey Avocado ", "Italian B.M.T", "Meatball Marinara", "Honey mustard rotisserie - style chicken"]  #(0,5)
Scarantinos_list = ["Fired mozzarella","Shrip cocktail","cup of minestrone soup", "Baked stuffed Lasagna", "Baked mostacciioli sorrento","Pasta Tino","Angle hair Tomato & Basil","Linguine with with clams"] #(0,8)
monster_sushi_list = ["Bay Scallop","Egg(tampago)","Califorina roll","Spicy tuna roll","Philly roll","Hawaiian roll","Mexican Roll","Playbot Roll","calamari tempura Roll"] #(0,9)
print("Please input the number next to the restautant you would like to eat at ")
print(restaurant_list)
e = int(input(" "))
g = 0
if (e == 0):
    print("Here is a item from the menu for subway ")
    g = random.randrange(-1,5)
    print(subway_list)
    print("I recomend you get the " + str(subway_list[g]))
elif (e == 1):
    print("Here is a item from the menu for Scarantinos ")
    g = random.randrange(-1,8)
    print(Scarantinos_list)
    print(" I recomend you get the " + str(Scarantinos_list[g]))
elif ( e == 2):
    print("Here is a item from the menu for monster Sushi ")
    g = random.randrange(-1,9)
    print(monster_sushi_list)
    print(" I recomend you get the " + str(monster_sushi_list[g]))
else:
    print("Your input is vaild")