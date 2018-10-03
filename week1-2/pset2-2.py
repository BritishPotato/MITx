# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:30:01 2017

@author: Denizhan Akar
"""
# Goal:
# lowest monthly payment to pay off all debt under 1 year


# Test Case 1:
balance = 3926
annualInterestRate = 0.2


updatedBalance = balance
lowestPay = 0

while updatedBalance >= 0: # Do until updatedBalance less than negative
    lowestPay += 10 # New check
    updatedBalance = balance # Reset updatedBalance
    # Does the monthly calculations for 12 months
    for i in range(12):
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = updatedBalance - lowestPay
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * \
                                             monthlyUnpaidBalance)

    
print("Lowest Payment: " + str(lowestPay))
