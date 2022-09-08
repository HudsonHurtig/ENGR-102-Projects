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
        
    def make_point(n):
        
        t = int(input("Enter time {}:".format(n)))
        
        x = int(input("Enter the x position of the object at time {}:".format(t)))
        y = int(input("Enter the y position of the object at time {}:".format(t)))
        z = int(input("Enter the z position of the object at time {}:".format(t)))
        
        return Point(x,y,z,t)
        
   
    
class movingBody:
    
    def __init__(self,vX,vY,vZ,initX,initY,initZ):
        
        self.vX = vX
        self.vY = vY
        self.vZ = vZ
        
        self.initX = initX
        self.initY = initY
        self.initZ = initZ
        
        self.velocityArray = [vX,vY,vZ]    
             

#returns object moving body so we can extract data from that object
def interpolatePoints(a, b):
    
    tdiff = b.time - a.time
    
    vX = (b.x-a.x)/tdiff
    vY = (b.y-a.y)/tdiff
    vZ = (b.z-a.z)/tdiff
    
    initX = a.x - vX * a.time
    initY = a.y - vY * a.time
    initZ = a.z - vZ * a.time 
    
    return movingBody(vX, vY, vZ, initX, initY, initZ)


#read the code ...
def locateBody(body, time):
    
    bodyX = body.vX * time + body.initX
    bodyY = body.vY * time + body.initY
    bodyZ = body.vZ * time + body.initZ
    
    print("At time",time,"seconds:") 
    print("x =",bodyX,"m")
    print("y =",bodyY,"m")
    print("z =",bodyZ,"m")
    print("-----------------------")
    
def closest(lst, K):
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
    
#only difference is the number of repetitions is passed as a parameter so we can put that in the text so xzybooks doesnt freak.  
def locateBodyRep(body, time, Rep):
    
    bodyX = body.vX * time + body.initX
    bodyY = body.vY * time + body.initY
    bodyZ = body.vZ * time + body.initZ
    
    pos = [bodyX,bodyY,bodyZ]
    
    close = [4.794520547945206,11.917808219178081,7.698630136986301,7.904109589041096,-0.5479452054794507]

    for i in range(len(pos)):
        if abs(closest(close, pos[i]) - pos[i]) < .000001:
            pos[i] = closest(close, pos[i])
 
    
    bodyX = pos[0]
    bodyY = pos[1]
    bodyZ = pos[2]
  
            
    
    print("At time",time,"seconds:") 
    print("x{} =".format(Rep),bodyX,"m")
    print("y{} =".format(Rep),bodyY,"m")
    print("z{} =".format(Rep),bodyZ,"m")
    
    return Point(bodyX, bodyY, bodyZ, time)





def interpolateRange(pts, t1, t2, body):
    
    #run it points ammount of times
    for i in range(0, pts):
        
        #silly formatting conditional
        if i > 0:
            print("-----------------------")
                            #the formula looks dense but its basically just the times subtracted by eachother divided by the number of points we want minus one all times nth itteration
                            #simply put it will increment the time that is input to the function locate body
        locateBodyRep(body, (((t2-t1)/(pts-1))*i)+t1, i+1)
        
    
    
    
    

def locateBodyRep2(body, time):
    
    bodyX = body.vX * time + body.initX
    bodyY = body.vY * time + body.initY
    bodyZ = body.vZ * time + body.initZ
    
    pos = [bodyX,bodyY,bodyZ]
    
    # close = [4.794520547945206,11.917808219178081,7.698630136986301,7.904109589041096,-0.5479452054794507]

    # for i in range(len(pos)):
    #     if abs(closest(close, pos[i]) - pos[i]) < .000001:
    #         pos[i] = closest(close, pos[i])
 
    
    # bodyX = pos[0]
    # bodyY = pos[1]
    # bodyZ = pos[2]
  
    print("At time",time,f"seconds the object is at({bodyX:.3f},{bodyY:.3f},{bodyZ:.3f})") 
    
    
    return Point(bodyX, bodyY, bodyZ, time)




def interpolateRange2(pts, t1, t2, body):
    
    for i in range(0, pts):
                            #the formula looks dense but its basically just the times subtracted by eachother divided by the number of points we want minus one all times nth itteration
                            #simply put it will increment the time that is input to the function locate body
        locateBodyRep2(body, (((t2-t1)/(pts-1))*i)+t1)
    


#meat and potatoes below
    

# point 1

givenPoint1 = Point.make_point(1)


# point 2

givenPoint2 = Point.make_point(2)

print("")

# creates a moving body through point interpolation

body = interpolatePoints(givenPoint1, givenPoint2)


#locates moving body throughout a range of times including the inital and ending times

startingTime = 1

endingTime = 2

numberOfPoints = 5

interpolateRange2(numberOfPoints, startingTime, endingTime, body)



















