# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 18:28:23 2017

@author: Denizhan Akar
"""

# Goal:
# lowest monthly payment to pay off all debt under 1 year
# Now with bisection search efficiency!


# Test Case 1:
balance = 999999
annualInterestRate = 0.18


monthlyInterestRate = annualInterestRate / 12.0
low = balance / 12.0
high = balance * (1 + monthlyInterestRate) ** 12 / 12.0

while True:
    lowestPay = (high + low) / 2
    updatedBalance = balance  # Reset updatedBalance
    for i in range(12):
        monthlyUnpaidBalance = updatedBalance - lowestPay
        updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate *
                                                 monthlyUnpaidBalance)
    if updatedBalance > 0.01:  # HOW TO GO DOWN TO THE CENT FOR LOWPAY? Done.
        low = lowestPay
    elif updatedBalance < -0.01:
        high = lowestPay
    else:
        break

print("Lowest Payment: " + str(round(lowestPay, 2)))

"""
Lesson: USE round() WITH CAUTION!!!
I see. It seems that one should use round() only at the very end in order to
ensure that lowestPay is not stuck in an infinite loop of alternating between
two rounded figures.
"""

progress = []
progress = progress.append("Source strings separated by white space are "
                           "automatically concatenated by the "
                           "interpreter and parenthesis are the natural "
                           "syntax for line continuation. Remember to use "
                           "trailing spaces.")
