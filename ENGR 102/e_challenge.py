# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson
# Section:      575
# Assignment:   Lab topic 2 individual
# Date:         9/8/22


from math import *


digits = int(input("Please enter the number of digits of precision for e:"))


stringTxt = '2.71828182845904523536028747135266249775724709369995'

def digs(num):
    
    lastVal = stringTxt[num+2]
    #print(stringTxt[0:num+1])
    if int(lastVal) > 4:
        
        
        output = stringTxt[0:num-1] + str(int(stringTxt[num]) + 1)
        
    else:
        
        output = stringTxt[0:num]
        
    return output
        
    

print("The value of e to",digits,"digits is:",digs(digits+2))
