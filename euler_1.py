#1 
print(sum([i for i in range(1000) if (i % 3 == 0 or i % 5 == 0)]))

#2 
a, b, fib = 0, 1, []
while b < ((4 * (10 ** 6))):
    a += b
    b += a
    fib.extend([a, b])
fib = sum(list(filter(lambda y: y < (4 * (10 ** 6)), filter(lambda x: x % 2 == 0, fib))))
print(fib)

#3

#4

#5

#6
print(((sum([i for i in range(101)]))**2) - sum([(i ** 2) for i in range(101)]))

#7
