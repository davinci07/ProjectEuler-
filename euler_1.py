multiples = []

for x in range(1,1000):
    if (x%3 == 0) or (x%5 ==0):
        multiples.append(x)
print (sum(multiples))