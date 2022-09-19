# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 4
# Date:         9-19-22
#


#silly comment

uin1 = float(input("Enter number 1:")) 
uin2 = float(input("Enter number 2:")) 
uin3 = float(input("Enter number 3:")) 

if uin1 > uin2 and uin1 > uin3:
    print("The largest number is", uin1)
elif uin2 > uin1 and uin2 > uin3:
    print("The largest number is", uin2)
else:
    print("The largest number is", uin3)