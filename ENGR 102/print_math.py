# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      505
# Assignment:   lab 1
# Date:         8-28-22
#


# this is some comment


#this imports all the math tools i need for this code
import math


#this next chunk prints both text and math!
mass = 3
acceleration = 5.5

v1 = mass * acceleration

distance = .025
theta = 25

v2 = 2 * distance * math.sin(theta * (math.pi/180))


grams = 5
days = 3
halfLife=3.8
v3 = grams * pow(2, -(days/halfLife))


moles = 5
temp = 415
idealConstant = 8.314
Vol = .25
v4 = ((moles*temp*idealConstant)/Vol)/1000

print("Force is", v1 ,"N")
print("Wavelength is", v2 ,"nm")
print("Radon-222 left is", v3 ,"g")
print("Pressure is",v4,"kPa")
     
      
