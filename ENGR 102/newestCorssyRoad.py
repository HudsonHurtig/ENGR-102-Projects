import sys
import os
import math
import time
import numpy as np
import keyboard
from collections import deque 
import keyboard


density = " ,-~:;=!*#$@"

startVal = 1
numColumns = 150
numRows = 10


# animation speeds

ticker = 0 #horizontal offset for sin wave functions
increment = .02 #speed of the horizontal offset

refreshRate = .01                


chickenX = 0
chickenY = 0

gameFrame = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def setChickenLocation(newX,newY):
    global chickenX 
    global chickenY 
    
    
    
    gameFrame[chickenY][chickenX] = 0
    
    
    chickenX += newX
    chickenY += newY
    
    gameFrame[chickenY][chickenX] = 11

    
def showBoard():
    for i in gameFrame:
        print(i)

def loose():
    
    global chickenX, chickenY
    
    if gameFrame[chickenY][chickenX+1] > 0 or gameFrame[chickenY][chickenX-1] > 0:
        return True
    else:
        return False

def win():
    
    if chickenY == 0:
        return True
    else:
        return False

def updateVisual():
    
    global ticker, increment
    ticker += increment
    
    
    gameFrame[1] = [3 * int(1 + 2*math.sin(i/5 + ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[2] = [2 * int(1 + 2*math.sin(i/10 - ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[3] = [3 * int(1 + 2*math.sin(i/6 + ticker)) for i in range(len(gameFrame[1]))]
    setChickenLocation(0, 0)
    
    for q in gameFrame: 
        for i in q:
            print(density[i], end='')
        print("\n")
   
   
   
setChickenLocation(80, 4)


     
while True:
    if loose():
        
        break
    
    elif win():
        
        break
    
    else:
        try:
            if keyboard.is_pressed('left'):
                if chickenX > 0:
                    setChickenLocation(-1, 0)
                
            if keyboard.is_pressed('right'):
                if chickenX < 159:
                    setChickenLocation(1, 0)
                
            if keyboard.is_pressed('down'):
                if chickenY < len(gameFrame)-1:
                    setChickenLocation(0, 1)
                
            if keyboard.is_pressed('up'):
                if chickenY > 0: 
                    setChickenLocation(0, -1)
        except:
            pass       
            
        updateVisual()
        
        
        
    time.sleep(refreshRate)
    os.system('cls')
    
if loose():
        
    print("GAME OVER")
    
    time.sleep(5)
    
elif win():
        
    print("why did the chicken cross the road? to win! congradulations")
    
    time.sleep(5)