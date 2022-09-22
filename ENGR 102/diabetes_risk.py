# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Avi Punjabi
#               MJ Murray
#               Hudson Hurtig
#               Gabriel Isaac
#               Brian Tran
# Section:      575
# Assignment:   Lab 5.3.1
# Date:         09 20 22
from math import *

#initializes the variables to be used in the risk formula, set to an arbitrary value of 0 for now
sexNum = 0
ageNum = 0
BMINum = 0
HMNum = 0
steroidsNum = 0
smokeNum = 0
histNum = 0

sexInput = input("Enter your sex (M/F): ") 
print("")

if sexInput == 'F' or sexInput == 'f': #determines what value to use for sex
    sexNum = 0.879
else:
    sexNum = 0

ageInput = float(input("Enter your age (years): ")) #because age is already a number, the input is converted to a float
print("")

ageNum = ageInput #determines what value to use for age

BMIInput = float(input("Enter your BMI: ")) #because BMI is already a number, the input is converted to a float
print("")

if BMIInput < 25: #determines what value to use for BMI
    BMINum = 0
elif BMIInput >= 25 and BMIInput < 27.5:
    BMINum = 0.699
elif BMIInput >= 27.5 and BMIInput < 30:
    BMINum = 1.97
else:
    BMINum = 2.518

HMInput = input("Are you on medication for hypertension (Y/N)? ") 
print("")

if HMInput == 'Y' or HMInput == 'y': #determines what value to use for hypertension medication
    HMNum = 1.222
else:
    HMNum = 0

steroidsInput = input("Are you on steroids (Y/N)? ") 
print("")

if steroidsInput == 'Y' or steroidsInput == 'y': #determines what value to use for steroids
    steroidsNum = 2.191
else:
    steroidsNum = 0

smokeInput = input("Do you smoke cigarettes (Y/N)? ") 
print("")

if smokeInput == 'Y' or smokeInput == 'y': #determines what value to use for smoking
    smokeNum = 0.855
else: #if they don't currently smoke, determines if they used to or never have
    smokeInputNew = input("Did you used to smoke (Y/N)? ")
    print("")

    if smokeInputNew == 'Y' or smokeInputNew == 'y':
        smokeNum = -0.218
    else:
        smokeNum = 0

histInput = input("Do you have a family history of diabetes (Y/N)? ")
print("")

if histInput == 'Y' or histInput == 'y': #determines what value to use for family history
    histInputNew = input("Both parent and sibling (Y/N)? ") #if they do have a family history, determines whether it was both a parent and sibling or just one of them

    if histInputNew == 'Y' or histInputNew == 'y':
        histNum = 0.753
    else:
        histNum = 0.728
else:
    histNum = 0

n = 6.322 + sexNum - (0.063 * ageNum) - BMINum - HMNum - steroidsNum - smokeNum - histNum #calculates n

risk = 100 / (1 + exp(n)) #calculates risk

print(f'Your risk of developing type-2 diabetes is {risk:.1f}%') 