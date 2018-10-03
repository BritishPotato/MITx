# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 02:13:32 2017

@author: Batuhan Akar
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    inc = 0
    for i in range(1, k +1):
        inc += i
        if inc == k:
            return True
    return False



is_triangular(1)

is_triangular(10)

is_triangular(11)

is_triangular(500)

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    sNew = ""
    for letter in s:
        if letter not in "aeiouAEIOU":
            sNew += letter
    print(sNew)
    
print_without_vowels("Go fuck yourself mate seriously!")
    
    
# UNDERSTOOD IT WRONG: "that occurs an odd number of times in L"!!!!!
def largest_odd_timesONLYCHECKSBIGGEST(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    check = -1
    for i in L:
        if i % 2 and i > check:
            check = i
    if check != -1:
        return check
  
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    occurDic = {}
    for i in L:
        if i not in occurDic:
            occurDic[i] = 0
        occurDic[i] += 1
    numberHighest = -1
    for number, frequency in occurDic.items():
        if frequency % 2 and number > numberHighest:
            numberHighest = number
    if numberHighest != -1:
        return numberHighest
    

largest_odd_times([2, 2, 4, 6, 4, 2])

"""
Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list (increasing order) of all keys in d that have the same value in d. 
Here are two examples:
If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newd = {}
    for key, value in d.items():
        if value not in newd:
            newd[value] = [key]
        else:
            newd[value] += [key]
            newd[value].sort()
            #newd[value].insert(0, key)
    return newd

dict_invert({1:10, 2:20, 3:30})
dict_invert({1:10, 2:20, 3:30, 4:30})
dict_invert({4:True, 2:True, 0:True})


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def function(x):
        result = 0
        k = len(L) - 1
        for num in L:
            result += num * x**(k)
            k -= 1
        return result
    return function

def is_list_permutationNOPE(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    occurDic = {}
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    for element in L1:
        if element not in L2:
            return False
        if element not in occurDic:
            occurDic[element] = 0
        occurDic[element] += 1
    frequencyHighest = 0
    for element, frequency in occurDic.items():
        if frequency > frequencyHighest:
            frequencyHighest = frequency
            frequentElement = element
    return (frequentElement, frequencyHighest, type(frequentElement))
    
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    occurDic1 = {}
    occurDic2 = {}
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    if len(L1) != len(L2):
        return False
    for element in L1:
        if element not in L2:
            return False
        if element not in occurDic1:
            occurDic1[element] = 0
        occurDic1[element] += 1
    for element in L2:
        if element not in occurDic2:
            occurDic2[element] = 0
        occurDic2[element] += 1
    frequencyHighest = 0
    for element, frequency in occurDic1.items():
        if occurDic1[element] != occurDic2[element]:
            return False
        if frequency > frequencyHighest:
            frequencyHighest = frequency
            frequentElement = element
    return (frequentElement, frequencyHighest, type(frequentElement))