#!/usr/bin/Python 3
import unittest

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
    

print(isEven(43))


class TestIsEvenMethod(unittest.TestCase):
     # Returns True or False.  
    def test_isEven1(self):         
        #self.assertTrue(isEven(5)) 
        #self.assertFalse(isEven(5)) 
        self.assertEqual(isEven(5), False)
    def test_isEven2(self):
        self.assertEqual(isEven(10), True)
    def test_isEven3(self):
       self.assertRaises(TypeError, isEven('hello'))
            


if __name__ == '__main__': 
    unittest.main() 

