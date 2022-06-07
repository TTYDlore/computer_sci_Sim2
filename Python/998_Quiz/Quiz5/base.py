s = input("What is your favorite number? ")
age = int(input("how old are you? "))
x = 0
num = 0
for i in s:
    if(s[x:x+1] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):  #why is line accpeting any char ?
        num = int(s[x:x+1])
        if(s[x + 1: x + 2] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
            num = int(s[x:x+2])
            if(s[x+2:x+3] == "0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
                num = int(s[x:x+3])
                break
            break
        break
    x = x + 1
number = (age * num)
print("Your favorite number times your age is " + str(number))