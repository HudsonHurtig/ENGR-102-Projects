# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 4
# Date:         9-19-22
#

import math
#silly comment 


a = int(input("Please enter the coefficient A:"))

b = int(input("Please enter the coefficient B:"))

c = int(input("Please enter the coefficient C:"))


discriminate = b * b - 4 * a * c 

sqrAbs = math.sqrt(abs(discriminate)) 

if discriminate > 0: 
    r1 = (-b + sqrAbs)/(2 * a)
    r2 = (-b - sqrAbs)/(2 * a)
    if r1 == r2:
        print(f"The root is x = {r1}")
    else:
        print(f"The root is x = {r1} and x = {r2}")
else:
    r1 = str(-b/(2*a))+" + i"+str(sqrAbs)
    r2 = str(-b/(2*a))+" - i"+str(sqrAbs)
    if r1 == r2:
        print(f"The root is x = {r1}")
    else:
        print(f"The root is x = {r1} and x = {r2}")
    
      

