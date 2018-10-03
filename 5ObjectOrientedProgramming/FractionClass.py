# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:55:19 2017

@author: Batuhan Akar
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
    def __str__(self):
        return str(self.numer) + " / " + str(self.denom)
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = self.getNumer() * other.getDenom() \
        + other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def __sub__(self, other):
        numerNew = self.getNumer() * other.getDenom() \
        - other.getNumer() * self.getDenom()
        denomNew = self.getDenom() * other.getDenom()
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()

oneHalf = fraction(1,2)
twoThirds = fraction(2,3)

print(oneHalf) # Out: 1 / 2
print(twoThirds) # Out: 2 / 3

print(oneHalf.getNumer()) # Out: 1
# this is a procedure, so must invoke by passing in arguments
# (empty argument in this case)

print(fraction.getDenom(twoThirds)) # Out: 3

print(oneHalf + twoThirds) # Out: 7 / 6

print(twoThirds.convert()) # Out: 0.6666666...
# ^^INSTANT OF CLASS^^.^^METHOD^^()

print(fraction.convert(twoThirds)) # Out: 0.66666...
# ^^CLASS^^.^^METHOD^^(^^INSTANT OF CLASS^^)

# getters and setters are seperate to make sure we do not
# directly manipulate objects