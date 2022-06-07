import random
compliantlist = [" is cool"," is fantastic"," is a girl boss","i s amazing"," is a good person"," is possobly a furry", " is smart"," is smart"]
peoplelist = ["you","U","Your mom","Your dad","your dog","your family","Your cosuin","Your firend",]

y = random.randrange(-1,len(peoplelist))
x = random.randrange(-1,len(compliantlist))
print(peoplelist[y] + compliantlist[x])
