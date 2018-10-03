# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:00:40 2017

@author: Batuhan Akar
"""

def genPrimes():
    yield 2
    num = 3
    primes = [2]
    while True:
        isPrime = True
        # for every prime in the list
        for prime in primes:
            # check if remainder becomes zero (not prime)
            if (num % prime) == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(num)
            yield num
        num += 1