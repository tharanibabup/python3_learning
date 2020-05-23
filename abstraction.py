
import math

class Point(object):
    def __init__(self, a, b, c):
        self._x = a
        self._y = b
        self._z = c 

    def __str__(self):
        return 'point : (x, y, z)'
    
    def distance(self, x1, x2, y1, y2, z1, z2):
        distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 + (z1 -z2)**2 )
        return distance

    def __add__(self, other):
       total_x = self._x + other._x
       total_y = self._y + other._y
       total_z = self._z + other._z

       return Point(total_x, total_y, total_z)


p1 = Point(4, 2, 9)
p2 = Point(4, 5, 6)
p3 = Point(-2, -1, 4)
print(p1)

x1 = p2._x 
x2 = p3._x 
y1 = p2._y
y2 = p3._y
z1 = p2._z
z2 = p3._z

dist = p1.distance(x1, x2, y1, y2, z1, z2)
print (dist)

tp = p2 + p3
print(tp._x)
print(tp._y)
print(tp._z)
