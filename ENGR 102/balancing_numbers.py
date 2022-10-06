# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


in1 = int(input("Enter a value for n:"))

left = int(((in1-1)*(1+(in1-1)))/2)

right = in1 + 1

r = 0

while left > right:
    r += 1
    right = int(((r)*((in1+1)+(in1+r)))/2)
    
    
    
    
if left == right:
    print(f"{in1} is a balancing number with r={r}") 
else:
    print(f"{in1} is not a balancing number")

# Enter a value for n: 102 
#  
 