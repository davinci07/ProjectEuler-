multiples = [long(x) for x in range(1,n) if((x % 3.0 == 0) or (x % 5.0 == 0))]
print (sum(multiples))
