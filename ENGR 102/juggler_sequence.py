# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment
import math

in1 = int(input("Enter a positive integer:"))
ls = []
print(f"The Juggler sequence starting at {in1} is:") 
count = 0
ls.append(str(in1))
while in1 != 1:
    
    if in1 % 2 != 0:
        in1 = math.pow(in1, 3)
        in1 = math.sqrt(in1)
        in1 = math.floor(in1)
        
    else:
        in1 = math.floor(math.sqrt(in1))
        
      
    ls.append(str(in1))
    
    count +=1

print(",".join(ls))
    

print(f"It took {count} iterations to reach 1 ")
 