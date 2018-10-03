# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:32:38 2016

@author: ericgrimson
"""

def selSort(L):
    compNum = 0
    for i in range(len(L) - 1):
        compNum += 8
        print(L)
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            compNum += 3
            if minVal > L[j]:
                compNum += 2
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
    print(compNum)

test = [3, 5, 9, 8, 4, 2, 1, 6]
selSort(test)
