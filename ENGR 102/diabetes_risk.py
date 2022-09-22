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

sexNum = 0
ageNum = 0
BMINum = 0
HMNum = 0
steroidsNum = 0
smokeNum = 0
histNum = 0

sexInput = input("Enter your sex (M/F): ") 

if sexInput == 'F':
    sexNum = 0.879
else:
    sexNum = 0

ageInput = float(input("Enter your age (years): ")) 

ageNum = ageInput

BMIInput = float(input("Enter your BMI: "))

if BMIInput < 25:
    BMINum = 0
elif BMIInput >= 25 and BMIInput < 27.5:
    BMINum = 0.699
elif BMIInput >= 27.5 and BMIInput < 30:
    BMINum = 1.97
else:
    BMINum = 2.518

HMInput = input("Are you on medication for hypertension (Y/N)? ") 

if HMInput == 'Y':
    HMNum = 1.222
else:
    HMNum = 0

steroidsInput = input("Are you on steroids (Y/N)? ") 

if steroidsInput == 'Y':
    steroidsNum = 2.191
else:
    steroidsNum = 0

smokeInput = input("Do you smoke cigarettes (Y/N)? ") 

if smokeInput == 'Y':
    smokeNum = 0.855
else:
    smokeInputNew = input("Did you smoke in the past (Y/N)? ")

    if smokeInputNew == 'Y':
        smokeNum = -0.218
    else:
        smokeNum = 0

histInput = input("Do you have a family history of diabetes (Y/N)? ")

if histInput == 'Y':
    histInputNew = input("Is it both a parent and a sibling (Y/N)? ")

    if histInputNew == 'Y':
        histNum = 0.753
    else:
        histNum = 0.728
else:
    histNum = 0

n = 6.322 + sexNum - (0.063 * ageNum) - BMINum - HMNum - steroidsNum - smokeNum - histNum

risk = 100 / (1 + exp(n))


print(f'Your risk of developing type-2 diabetes is {risk:.2f}%')