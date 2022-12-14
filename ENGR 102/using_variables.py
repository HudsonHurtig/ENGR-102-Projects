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

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg):"))
acceleration = float(input("Please enter the acceleration (m/s^2):"))
v1 = mass * acceleration


print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm):"))
theta = float(input("Please enter the angle (degrees):"))

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

print(f"Force is {v1:.1f} N")
print(f"Wavelength is {v2:.4f} nm")
print(f"Radon-222 left is {v3:.2f} g")
print(f"Pressure is {v4:.0f} kPa")
     
      
