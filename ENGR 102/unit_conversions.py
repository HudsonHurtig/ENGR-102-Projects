import math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson
# Section:      506
# Assignment:   Lab topic 3 individual
# Date:         9/8/22


num_units = float(input("Please enter the quantity to be converted: "))

newtons = num_units * 4.45
feet = num_units * 3.28
kilopascals = num_units * 101.33

print(f"{num_units:.2f} pounds force is equivalent to {newtons:.2f} Newtons")
print(f"{num_units:.2f} meters is equivalent to {feet:.2f} Feet")
print(f"{num_units:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")




