import math

payment = int(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = payment-cost

print(math.exp(2))
                  
print(f"You received ${change} in change. That is...")

numQuarters = int((change-(change%.25))/.25)
print(numQuarters, "quarters")
change = round(change - (numQuarters * .25), 3)
print(change)

numNickels = int((change-(change%.1))/.1)
print(numNickels, "nickels")
change = change - (numNickels * .1)
print(change)

numDimes = int((change-(change%.1))/.1)
print(numDimes, "dimes")
change = change - (numDimes * .1)
print(change)

numPennies = int((change-(change%.1))/.1)
print(numPennies, "pennies")
change = change - (numPennies * .1)
print(change)



