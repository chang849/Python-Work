# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 13:37:37 2021

@author: sethc
"""



num = int(input("Enter number of bagels: "))
if num < 6:
 cost = 0.75 * num
else:
 cost = 0.6 * num
 print("Cost is ${0:,.2f}.".format(cost))

scores = []
scores.append(eval(input("Enter first score: ")))
scores.append(eval(input("Enter second score: ")))
scores.append(eval(input("Enter third score: ")))
scores.remove(min(scores))
average = sum(scores) / 2
print ("Average of the two highest scores is {0:.2f}" ,format(average))


balance = float(input("Enter current balance: "))
amountOfWithdrawal = float(input("Enter amount of withdrawal:"))
if (balance >= amountOfWithdrawal):
 balance -= amountOfWithdrawal
 print("The new balance is ${0:,.2f}.".format(balance))
 if balance < 150: print("Balance below $150", "Warning")
 else: print("Withdrawal denied.")
 
 
 
 
letter = input ("Enter a single uppercase letter:")
if (len(letter) !=1) or (letter !=letter.upper()):
  print("You did not comply with the request.")