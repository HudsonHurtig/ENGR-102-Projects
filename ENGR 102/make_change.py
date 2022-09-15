# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Hudson Hurtig
#               Avi Punjabi
#               Brian Tran
#               MJ Murray
#               Gabriel Isaac
# Section:      575
# Assignment:   Lab #4
# Date:         9-15-2022

import math

#taking input and defining vars
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = payment-cost

def plural(num):
    if num > 1:
        return 's'
    else:
        return ''
                  
print(f"You received ${change:.2f} in change. That is...")

numQuarters = int((change-(change%.25))/.25)

change = round(change - (numQuarters * .25), 5)
if numQuarters != 0:
    print(numQuarters, f"quarter{plural(numQuarters)}")
#print(change)

numDimes = int((change-(change%.1))/.1)

change = round(change - (numDimes * .1), 5)
if numDimes != 0:
    print(numDimes, f"dime{plural(numDimes)}")

#print(change)

numNickels = round(int((change-(change%.05))/.05),5)

change = change - (numNickels * .05)
if numNickels != 0:
    print(numNickels, f"nickel{plural(numNickels)}")
#print(change)

numPennies = int((change/.01))

if numPennies != 0:
    if numPennies == 1:
        print("1 penny")
    else:
        print(numPennies, f"pennie{plural(numPennies)}")




