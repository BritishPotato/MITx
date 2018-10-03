# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjk
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    value = 0
    check = False
    for i in s:
        try:
            value += int(i)
            check = True
        except:
            pass
    if check == False:
        raise ValueError
    return value

sum_digits("a;35d4")