# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      505
# Assignment:   lab 1
# Date:         8-28-22
#


# comment

import math

print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")

print("My guess is 2 \n")

q = 1.1

print(((q ** 2)-1)/(q-1))

for x in range(0,7):
    
    q = q - .09 * math.pow(10, -x)
    
#print('''2.1
#2.009999999999999
#2.0009999999999177
#2.0000999999993923
#2.0000100000008274
#2.0000010000889006
#2.000000099920072
#2.0\n''')
    
    print(((q ** 2)-1)/(q-1))
    


print("my guess was right!")
