# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:43:30 2017

@author: Batuhan Akar
"""

# Weird.getX() and .getY() gives error because
# it should have either added x,y to the parameters in
# the methods or written self.x and self.y instead of x and y
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w4 = Wild(X, 18)
print(w4.getX()) # Out: 7

X = w4.getX() + 17 + 7
print(X) # Out: 31

print(w4.getX()) # Out: 7
# This is because w4.get() is always going to retrieve the value specified in
# the __init__ routine, no matter what happens to the variable X. 
# They are two different things entirely.

# You would need to do
# w4 = Wild(X, 18)
# again for w4.x to change to 31