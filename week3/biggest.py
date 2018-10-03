# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:23:50 2017

@author: Denizhan Akar
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])

biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []})