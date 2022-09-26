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
        
        self.m = math.log(y1/y0)/math.log(x1/x0)
        
        self.arr = [self.lb,self.ub,x0,x1,y0,y1,self.m]
    
    def getPointAt(self, x):
        
        
        return self.y0 * pow(x/self.x0, self.m)
    
    def getBounds(self):
        
        return [self.lb, self.ub]
 
   
    
class PieceWise:
    
    
    def __init__(self,*arg):
        
        l1 = []
        l2 = []
        for i in arg:
            l1.append(i)
        self.equations = l1
        self.unions = []
        
    def addUnions(self, x, y):
        
        un = self.unions
        
        un.append([x,y])
        
        self.unions = un
        
    def getUnions(self):
        
        return self.unions
        

    def getValue(self, x):
        
        l1 = self.equations
        unions = self.getUnions()
        
        for q in range(len(l1)-1):
            
            bounds = l1[q].getBounds()
            
            
            for i in unions:
                
                if i[0] == x:
                    return i[1]
                
           
            if bounds[0] < x < bounds[1]:
                
                return l1[q].getPointAt(x)
            
        
                
            
        

        
    
        
c1 =   Curve(1, 2, 3, 4)
    
c2 = Curve(2, 3, 5, 5)      

piec = PieceWise(c1, c2, c2)



piec.addUnions(1.3, 1000)  
piec.addUnions(5, 7000)  
piec.addUnions(30, 150000)  
piec.addUnions(120, 25000)  
piec.addUnions(1200, 1500000) 

print(piec.getValue(5))


    


    

        
    