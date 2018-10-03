# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:02:34 2017

@author: Batuhan Akar
"""

from matplotlib import pylab as plt

# plt.<procName>

mySamples = []
kek = []
top = []

for i in range(30):
    mySamples.append(i)
    kek.append(i**2)
    top.append(1.5**i)

plt.figure("quackkkk")
plt.title("this is gud")
plt.ylabel("y")
plt.xlabel("x")
plt.ylim(0, 200)
# plt.clf()  # Clean display.S

# First string --> color
# b --> blue
# r --> red
# g --> green
# k --> black

# Second string --> how to do display
# - --> line
# o --> circle
# ^ --> triangle
# -- --> dash
plt.subplot(121) # (num of rows)(num of cols)(which location)
plt.plot(mySamples, kek, "ro", label = "kekorino")
plt.plot(mySamples, top, "k--", label = "topolol", linewidth = 10)
plt.yscale("log") # increase of order in magnitude
plt.legend()
plt.title("better")