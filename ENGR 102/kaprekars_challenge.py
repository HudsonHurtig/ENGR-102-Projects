
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


import math

def errorMessage():
    print("ERROR")
    
    
def normalizeVarible(q):
    
    if type(q) != str():
        q = str(q)
        
    l = list(q)
    while len(l) < 4:
        l.insert(0,'0')

        
    return l

def isPlayable(q):
    
    return not(all([q[0] == q[i] for i in range(len(q))]))

def toInt(l):
    
    return int("".join(l))


def findK(l):
    
    v1 = [int(l[q]) for q in range(len(l))]
    v1.sort()
    v2 = v1[::-1]
    
    v1 = [str(v1[q]) for q in range(len(v1))]
    v2 = [str(v2[q]) for q in range(len(v2))]
    
    v1 = toInt(v1)
    v2 = toInt(v2)
    
    return abs(v1-v2)
    
    
def find_iterations(o):
     
    o = str(o)

    in1 = normalizeVarible(o)

    if isPlayable(in1):
        k = 0
        counter = 0
        p = []
        while k != 6174:
            counter += 1
        
            k = findK(in1)
            in1 = normalizeVarible(k)
            p.append(k)
            
        
        p = [str(p[q]) for q in range(len(p))]

        # print(o,">"," > ".join(p)) 
        
        # print(f"{o} reaches 6174 via Kaprekar's routine in {counter} iterations")
        
        return counter
        
    else:
        
        k = 0
        counter = 0
        p = []
        while k != 0:
            counter += 1
        
            k = findK(in1)
            in1 = normalizeVarible(k)
            p.append(k)
            
        
        p = [str(p[q]) for q in range(len(p))]

        # print(o,">","0") 
        
        # print(f"{o} reaches 0 via Kaprekar's routine in 1 iterations")
        
        return 1
    

count = 0  
for i in range(1,9999):
    count += find_iterations(i)

print(f"Kaprekar's routine takes {count} total iterations for all four-digit numbers")    
    
    
    
        
    

