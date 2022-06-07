x = input("Please enter your first and last name EX: Jacob Poole ")
space = 0
o = 0
for v in x:
    if(x[0 + o] == " "):
        space = x[0 + o]
        break
    o = o + 1
first = x[0 + o - 1]
a = 1
c = 0
print("")
for i in range(0 + o + 1,len(x)):
    b = x[0 + o + a:1 + o + a]
    a = a + 1
    print(b)
print(" ")
for t in range(0,0 + o):
    u = x[0 + c:1 + c]
    print(u)
    c = c + 1
