# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

### GO DOWN IN ORDER

# object = self (= the instance of the class)
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        result = (x_diff_sq + y_diff_sq)**0.5
        return result
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
kek = Coordinate(3, 4)

# kek.distance(3,2) --> no, this makes 3 args (self is include)
# kek.distance(3) --> no, this is only an int


top = Coordinate(0, 0)
print(kek.distance(top)) # Out: 5.0
# jaja correct!
# This is the conventional way.
# kek = object on which method is called upon
# distance = name of method
# (top) = parameters not including self because self
# is implied to be kek

# However, you can also do this:
print(Coordinate.distance(kek, top)) # Out: 5.0
# Coordinate = name of class
# distance = name of method
# (kek, top) = parameters, including an object (kek) which
# to call the method, representing the self

print(kek) # Out: <__main__.Coordinate object at 0x0000024233FF4C50>
# Not very helpful, nope.

# This is why we use the __str__ method for a class!
# Python calls this when used with print() on your class object.
# You choose what it does! ( ͡° ͜ʖ ͡°) 
# Uncomment __str__ to see it in action

print(type(kek)) # Out: <class '__main__.Coordinate'>
# Makes sense because
print(type(Coordinate)) # Out: <class 'type'>

print(isinstance(kek, Coordinate)) # Out: True
# Use isinstance() to check if an object is an instance of a class

# Then there are SPECIAL OPERATORS which you can OVERRIDE
# Define them with double underscore before/after
# __add__(self, other) --> self + other
# __sub__(self, other) --> self - other
# __eq__(self, other) --> self == other
# __lt__(self, other) --> self < other
# __len__(self, other) --> len(self)
# __str__(self, other) --> print(self)

subby = top-kek
print(subby)


### COMMENT OUT __str__ BEFORE SAVING TO LEAVE