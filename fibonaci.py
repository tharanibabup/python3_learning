
def fib_gen(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1

li = [0,1,2,3,4]

for l in li:
    fs = fib_gen(l)
    cont = 0 
    for i in fs:
        cont = i
    print (i)


