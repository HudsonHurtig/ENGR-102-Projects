# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 4
# Date:         9-19-22
#

############ Part A ############

#silly comment 

a = 1 / 7         
print(f'a = {a}') 
b = a * 7         
print(f'b = a * 7 = {b}') 

#yes its 1

c = 2 * a
d = 5 * a 
f = c + d 
print(f'f = 2 * a + 5 * a = {f}') 

# no it is not 1

from math import sqrt 
x = sqrt(1 / 3)    
print(f'x = {x}') 
y = x * x * 3     
print(f'y = x * x * 3 = {y}') 
z = x * 3 * x     
print(f'z = x * 3 * x = {z}')

TOL = 1e-10 

if abs(y - z) < TOL: 
    
    print(f'y and z are equal within tolerance of {TOL}') 
    
else:                 
    
    print(f'y and z are NOT equal within tolerance of {TOL}') 

# no it is not 1

############ Part B ############

TOL = 1e-10 

if abs(b - f) < TOL: 
    
    print(f'b and f are equal within tolerance of {TOL}') 
    
else:                 
    
    print(f'b and f are NOT equal within tolerance of {TOL}') 
    

    