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
        elif days >= 11 and days <= 60:
            out = 10 * 5 + (days-10) * 50
        elif days >= 61 and days <= 101:
            
            out = int(2550 + ((49+(110-days))/2)*(days-60))
        print(f"The total number of gadge ts produced on day {days} is {out}")
    else:
        print("You entered an invalid number!")

except:
    print("You entered an invalid number!")
