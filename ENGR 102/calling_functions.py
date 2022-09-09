# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Hudson
# Section:      575
# Assignment:   Lab topic 3 individual
# Date:         9/8/22

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')


#area of polygon is (num_sides*lenth)/4tan(pi/num_sides)

def getArea(s_length, n_sides):
    return n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
    
    
    
# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

length = float(input("Please enter the side length:"))
printresult('triangle', length, getArea(length, 3))
printresult('square', length, pow(length,2))
printresult('pentagon', length, getArea(length, 5))
printresult('dodecagon', length, getArea(length, 12))