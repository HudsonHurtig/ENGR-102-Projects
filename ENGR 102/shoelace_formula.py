# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Avi Punjabi
#               MJ Murray
#               Hudson Hurtig
#               Gabriel Isaac
#               Brian Tran
# Section:      575
# Assignment:   Lab 7
# Date:         10 07 22

#sillly comment

# Please enter the vertices: 3,4 5,6 9,5 12,8 5,11 
# The area of the polygon is 30.0 

def getpoints(stringOfPoints):
    
    points = [i.split(",") for i in stringOfPoints.split()] #splits using spaces and commas
    points = [list(map(int, i)) for i in points] # converts to interger

    return points

def cross(point1, point2):
    
    a,b = point1
    c,d = point2
    
    return a * d - b * c

def shoelace(in1):
    
    in1.append(in1[0]) # append last point for 
    summation = 0
    
    for i in range(len(in1)-1):
        
        summation += cross(in1[i], in1[i+1]) # take cross product of all points and add them up
    
    return summation/2 #return summation devided by two
    
    
def main():
    user_input = input("Please enter the vertices: ")
    
    pts = getpoints(user_input)
    
    print("The area of the polygon is", shoelace(pts))
    



if __name__ == '__main__': 
    main() 
    
    
