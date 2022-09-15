import math

payment = int(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = payment-cost

                  
print(f"You received ${change} in change. That is...")

numQuarters = int((change-(change%.25))/.25)

change = round(change - (numQuarters * .25), 4)
if numQuarters != 0:
    print(numQuarters, "quarters")
#print(change)

numNickels = int((change-(change%.1))/.1)

change = change - (numNickels * .1)
if numNickels != 0:
    print(numNickels, "nickels")

#print(change)

numDimes = int((change-(change%.05))/.05)

change = change - (numDimes * .05)
if numDimes != 0:
    print(numDimes, "dimes")
#print(change)

numPennies = int((change/.01))

if numPennies != 0:
    print(numPennies, "pennies")




