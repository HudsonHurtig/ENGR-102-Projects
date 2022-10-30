# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


import math

def parta(rs, rh):
    #comment
    return 4/3 * math.pi * (rs**2 - rh**2)**1.5

#style comment
def partb(n):
    
    c = getConsec(n)
    s = -1 
    #comment
    
    for i in range(len(c)):
        if c[i] + c[min(i+1, len(c)-1)] == n:
            return [c[i], c[i+1]]
        elif c[i] + c[min(i+1, len(c)-1)] + c[min(i+2, len(c)-1)] == n:
            return [c[i], c[i+1], c[i+2]]
        
    return False
            
    
    
        
            
        
        
    
def getConsec(n):
    nums = [1, 3]
    #comment
    while nums[-1]+2 < n:
        nums.append(nums[-1] + 2)
    
    return nums    
            
def partc(*params):
    #comment
    length = max([len(i) for i in params]) + 4
    
    
    
    return params[0] * (length+2) + '\n' + params[0] + params[1].center(length, " ") + params[0] + '\n' + params[0] + params[2].center(length, " ") + params[0] + '\n' + params[0] + params[3].center(length, " ") + params[0] + '\n' + params[0] * (length+2) + '\n'
  
def partd(l):
    #comment
    return (min(l), int(sum(l)/len(l)), max(l))



def parte(l1,l2):
    #comment
    return [((l2[i] - l2[i+1])/(l1[i] - l1[i+1]))  for i in range(len(l1)-1)]
            




def partf(l1):
    #comment
    for i in l1:
        
        l1.pop(l1.index(i))
        
        for q in l1:
            
            if i + q == 2026:
                
                return i * q
            
        l1.append(i)
        
    return False
            
    
