payment = int(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = payment-cost

def how_many_of(c, val):
    return int((val - (val%c)) / c)
def remaineder_of(c, val):
    return (val%c)
print(f"You received ${change} in change. That is...")

print(how_many_of(.25, change), "quarters")
change = remaineder_of(.25, change)
print(change)
print(how_many_of(.1, change), "nickels")
change = remaineder_of(.1, change)
print(change)
print(how_many_of(.05, change), "dimes")
change = remaineder_of(.05, change)
print(change)
print(how_many_of(.01, change), "pennies")
change = remaineder_of(.01, change)
print(change)


