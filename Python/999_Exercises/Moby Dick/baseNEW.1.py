sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
whale_Count = 0
E = ""
b = 0
print(E)
for a in sentence:
    whale_Count = sentence[0 + b: 5 + b]
    if E == "whale":
        whale_Count = whale_Count + 1
    print(sentence[0 + b])
    print(whale_Count)
    b = b + 1
print("the sentence says whale " + str(whale_Count) + " times.")












#with open('moby.txt') as f:
#    for line in f:
#        sentence = line.strip()
#        ##YOUR CODE GOES HERE
#
#f.close()
