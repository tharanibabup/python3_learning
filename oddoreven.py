import itertools 

def even_or_odd(x):
    if (x%2 == 0):
        return 'even'
    else:
        return 'odd'

n = [10, 14, 16, 22, 9, 3 , 37]

for key, group in itertools.groupby(n, even_or_odd): 
    print(key, list(group)) 
