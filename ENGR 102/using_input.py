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
print(f"Force is {v1:.1f} N\n")

print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm):"))
theta = float(input("Please enter the angle (degrees):"))
v2 = 2 * distance * math.sin(theta * (math.pi/180))
print(f"Wavelength is {v2:.4f} nm\n")


print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days):"))
grams = float(input("Please enter the initial amount (g):"))

halfLife=3.8
v3 = grams * pow(2, -(days/halfLife))
print(f"Radon-222 left is {v3:.2f} g\n")



print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles:"))

Vol = float(input("Please enter the volume (m^3):")) 
temp = float(input("Please enter the temperature (K):"))

idealConstant = 8.314

v4 = ((moles*temp*idealConstant)/Vol)/1000
print(f"Pressure is {v4:.0f} kPa\n")
     
      
