
def factorial_gen(n):
    start = 0
    fact = 1
    while start <= n :
       yield fact
       start = start + 1
       fact = fact * start

li = [0,1,2,3,4]

for l in li:
    fs = factorial_gen(l)
    cont = 0 
    for i in fs:
        cont = i
    print (i)


