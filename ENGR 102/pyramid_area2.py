# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Hudson Hurtig
#               Avi Punjabi
#               Brian Tran
#               MJ Murray
#               Gabriel Isaac
# Section:      575
# Assignment:   Lab #4
# Date:         9-15-2022

#whittle comment

import math

L = float(input("Enter the side length in meters: "))
N = float(input("Enter the number of layers:"))

print(f"You need {(((math.sqrt(3)/4)*((L*N)**2))+(3*(N*(N+1))*L**2)/2):.2f} m^2 of gold foil to cover the pyramid")