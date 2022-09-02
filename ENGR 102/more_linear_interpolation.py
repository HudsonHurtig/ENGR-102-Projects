# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson
# Section:      506
# Assignment:   Lab topic 2 individual
# Date:         9/2/22


class Point:
    
    def __init__(self,x,y,z,time):
        
        self.x = x
        self.y = y
        self.z = z
        self.time = time
        
        self.arr = [x,y,z,time]
    
class movingBody:
    
    def __init__(self,vX,vY,vZ):
        
        self.vX = vX
        self.vY = vY
        self.vZ = vZ
        
        self.velocityArray = [vX,vY,vZ]
        
        
        


def interpolatePoints(a, b):
    
    tdiff = b.time - a.time
    
    vX = (b.x-a.x)/tdiff
    vY = (b.y-a.y)/tdiff
    vZ = (b.z-a.z)/tdiff
    
    return movingBody(vX, vY, vZ)



def locateBody(body, time):
    
    bodyX = body.vX * time
    bodyY = body.vY * time
    bodyZ = body.vZ * time
    
    return Point(bodyX, bodyY, bodyZ, time)
    
    
    

# point 1

point1 = Point(8,6,7,12)

# point 2

point2 = Point(-5,30,9,85)


# creates a moving body

body = interpolatePoints(point1, point2)







