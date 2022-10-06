# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 5
# Date:         9-22-22


# silly comment
import math

#curve class
class Curve:
    
    def __init__(self, x0,x1,y0,y1):
        
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.lb = x0
        self.ub = x1
        
        
        self.arr = [self.lb,self.ub,x0,x1,y0,y1]
    
    def getPointAt(self, x):
        
        x0 = self.x0
        y0 = self.y0
        x1 = self.x1
        y1 = self.y1
        
        logy = math.log10(y1/y0)
        logx = math.log10(x1/x0)
         
        m = logy/logx
        
        

        
        return ((y0) * ((x/x0) ** m))
    
    def getBounds(self):
        
        return [self.lb, self.ub]
 
#piece wise class
    
class PieceWise:
    
    #an unlimited number of fuctions can be passed as long as they are curve objects
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
        
        for q in range(len(l1)):
            
            bounds = l1[q].getBounds()
            
            
            for i in unions:
                
                if i[0] == x:
                    
                    return i[1]
                
                else:
                    
                    if bounds[0] < x < bounds[1]:
                      
                        return l1[q].getPointAt(x)
                    
                
#using objects 

#using object functions to process the union points and their values        
            
            


c1 = Curve(1.3, 5, 1000, 7000)
c2 = Curve(5, 30, 7000, 1500000)
c3 = Curve(30, 120, 1500000, 25000)
c4 = Curve(120, 1200, 25000, 1500000)

piec = PieceWise(c1,c2,c3,c4)

piec.addUnions(1.3, 1000)  
piec.addUnions(5, 7000)  
piec.addUnions(30, 150000) 
piec.addUnions(120, 25000) 
piec.addUnions(1200, 1500000)

in1 = float(input("Enter the excess temperature: "))

if 1200 >= in1 > 0:
    print(f"The surface heat flux is approximately {round(piec.getValue(in1))} W/m^2")
else:
    print("Surface heat flux is not available")

            




    


    

        
    