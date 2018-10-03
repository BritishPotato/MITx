# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:18:20 2017

@author: Denizhan Akar
"""

def printMove(fr, to):
	print("move from " + str(fr) + " to " + str(to))
    
def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
        
print(Towers(1, "first stack", "second stack", "third stack"))