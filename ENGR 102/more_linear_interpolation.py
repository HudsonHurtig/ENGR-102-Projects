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
    
    def __init__(self,vX,vY,vZ,initX,initY,initZ):
        
        self.vX = vX
        self.vY = vY
        self.vZ = vZ
        
        self.initX = initX
        self.initY = initY
        self.initZ = initZ
        
        self.velocityArray = [vX,vY,vZ]         


def interpolatePoints(a, b):
    
    tdiff = b.time - a.time
    
    vX = (b.x-a.x)/tdiff
    vY = (b.y-a.y)/tdiff
    vZ = (b.z-a.z)/tdiff
    
    initX = a.x - vX * a.time
    initY = a.y - vY * a.time
    initZ = a.z - vZ * a.time 
    
    print(initX)
    return movingBody(vX, vY, vZ, initX, initY, initZ)


def locateBody(body, time):
    
    bodyX = body.vX * time + body.initX
    bodyY = body.vY * time + body.initY
    bodyZ = body.vZ * time + body.initZ
    
    print("At time",time,"seconds:") 
    print("x1 =",bodyX,"m")
    print("y1 =",bodyY,"m")
    print("z1 =",bodyZ,"m")
    print("-----------------------")
    
    return Point(bodyX, bodyY, bodyZ, time)

def interpolateRange(pts, t1, t2, body):
    
    for i in range(0, pts):
        locateBody(body, (((t2-t1)/(pts-1))*i)+t1)
    
    
    

# point 1

givenPoint1 = Point(8,6,7,12)


# point 2

givenPoint2 = Point(-5,30,9,85)


# creates a moving body through point interpolation

body = interpolatePoints(givenPoint1, givenPoint2)

#locates moving body at time



startingTime = 12

endingTime = 85

numberOfPoints = 5


locateBody(body, 30)

interpolateRange(numberOfPoints, startingTime, endingTime, body)



















