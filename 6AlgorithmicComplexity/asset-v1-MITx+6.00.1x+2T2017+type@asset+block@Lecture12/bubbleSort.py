# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:06:53 2016

@author: WELG
"""

def bubble_sort(L):
    swap = False
    compNum = 1
    while not swap:
        swap = True  # If no longer swapped, this will remain True, breaking loop.
        print("\n", L)  # Show one element moved to correct place.
        compNum += 2
        for j in range(1, len(L)):
            compNum += 1
            print("for " + str(L))
            if L[j-1] > L[j]:  # If the elem before is greater than this element.
                compNum += 4
                print(L[j-1], L[j])
                swap = False
                L[j], L[j-1] = L[j-1], L[j]  # Swap both elements.
    print(compNum)

test = [3, 5, 9, 8, 4, 2, 1, 6]

bubble_sort(test)