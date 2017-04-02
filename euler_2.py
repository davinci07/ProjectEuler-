def fib(n):
    fib1 = [0,1]
    evenfib = []
    for x in range(1,n):
        fib1.append(fib1[x] + fib1[x - 1])
    for z in range(n):
        if fib1[z] >= (4 * (10 ** 6)):
            break
        if fib1[z] % 2 == 0:
            evenfib.append(fib1[z])
    print sum(evenfib)
fib(100)
