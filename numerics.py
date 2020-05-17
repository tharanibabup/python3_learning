


#x = .1 + .1 + .1 - .3
#print('x is {}' .format(x))
#print(type(x))


from decimal import *

a = Decimal('.10')
b = Decimal('.30')

x = a + a + a - b
print('x is {}' .format(x))
print(type(x))