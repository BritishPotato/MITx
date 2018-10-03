# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:17:09 2017

@author: Denizhan Akar
"""

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    
    # Updates to new balance for each month, round by 2
    balance = round(monthlyUnpaidBalance + (monthlyInterestRate * \
                                      monthlyUnpaidBalance), 2)
#    print(balance)


print("Remaining balance: " + str(balance))