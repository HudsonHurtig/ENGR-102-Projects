import math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson
# Section:      506
# Assignment:   Lab topic 3 individual
# Date:         9/8/22


#silly useless comment


num_units = float(input("Please enter the quantity to be converted: "))

newtons = num_units * 4.44822
feet = num_units * 3.28084
kilopascals = num_units * 101.325
BTUHR = num_units * 3.4121416331
galMin = num_units * 15.850323141
farenheit = (9/5)*num_units + 32

print(f"{num_units:.2f} pounds force is equivalent to {newtons:.2f} Newtons")
print(f"{num_units:.2f} meters is equivalent to {feet:.2f} feet")
print(f"{num_units:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")

print(f"{num_units:.2f} watts is equivalent to {BTUHR:.2f} BTU per hour")
print(f"{num_units:.2f} liters per second is equivalent to {galMin:.2f} US gallons per minute")
print(f"{num_units:.2f} degrees Celsius is equivalent to {farenheit:.2f} degrees Fahrenheit")




