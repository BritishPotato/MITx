# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 00:09:38 2017

@author: HP
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    for i in t:
        if isinstance(i, tuple) or isinstance(i, list):
            i = max_val(i)
        try:
            if check < i:
                check = i
        except UnboundLocalError:
            check = i
    return check
    
    
max_val((5, (1,2), [[1],[2]]))
max_val((5, (1,2), [[1],[9]]))