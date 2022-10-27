# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


import math

def parta(r,a):
    h = r - math.sqrt(r ** 2 - a ** 2)
    volcap = math.pi / 3 * (h ** 2) * (3 * r - h)
    return volcap


# def partb(n):
    
    
    
            
def partc(*params):
    
    length = max([len(i) for i in params]) + 4
    
    
    
    return params[0] * (length+2) + '\n' + params[0] + params[1].center(length, " ") + params[0] + '\n' + params[0] + params[2].center(length, " ") + params[0] + '\n' + params[0] + params[3].center(length, " ") + params[0] + '\n' + params[0] * (length+2) + '\n'
  
def partd(l):
    
    return [min(l), sum(l)/len(l), max(l)]

print(parta(2, 1))
 
print(partc('*', 'Dr. Ritchey', 'Texas A&M University', 
'snritchey@tamu.edu'))

print(partd([0,1,2]))


    
    
            
    

