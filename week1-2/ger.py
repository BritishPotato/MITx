from math import *

def polysum(n, s):
    return round((.25*n*s**2)/tan(pi/n)+(n*s)**2, 4)