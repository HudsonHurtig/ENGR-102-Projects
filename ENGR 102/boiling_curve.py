# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 5
# Date:         9-22-22


# silly comment
import math

class Curve:
    
    def __init__(self, x0,x1,y0,y1):
        
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.lb = x0
        self.ub = x1
        
        m = math.log(y1/y0)/math.log(x1/x0)
        
        self.arr = [self.lb,self.ub,x0,x1,y0,y1,m]
    
    def getPointAt(x):
        
        
        return self.y0 * pow(x/self.x0, self.m)
    
    def getBounds():
        
        return [self.lb, self.ub]
 
   
    
class PieceWise:
    
    
    def __init__(self,*arg):
        
        l1 = []
        l2 = []
        for i in arg:
            l1.append(i)
        self.equations = l1
        
        for i in arg:
            q = [i.lb,i.ub]
            l2.append(q)
        self.bounds = l2
        
    def getVal(x):
            
        for i in len(self.l2):
            if self.l2[0] < x < self.l2[1]:
                return "yes"
        
    
        
    
    
            

piec = PieceWise(Curve(1, 2, 3, 4), Curve(2, 3, 5, 5))
    
print(piec.getVal(1.4))
        
    
    
        
    