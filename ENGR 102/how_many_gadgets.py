# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 4
# Date:         9-19-22
#


#silly comment 

try:
    days = int(input("Please enter a positive value for day:"))
    if days > 0:
        if days < 11:
            out = days * 5
        elif days >= 11 or inp <= 60:
            out = 10 * 5 + (days-10) * 50
        elif days >= 61 or inp <= 101:
            p = days - 61
            out = 10 * 5 + (60) * 50 + ((-.5*days**2 + 100 * days) - (-.5*61**2 + 100 * 61))
        print(f"The total number of gadgets produced on day {days} is {out}")
    else:
        print("You entered an invalid number!")

except:
    print("You entered an invalid number!")
