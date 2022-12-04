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
    """prints out board"""
    for i in gameFrame:
        print(i)

def loose():
    """checks for loss"""
    global chickenX, chickenY
    
    if gameFrame[chickenY][chickenX+1] > 0 or gameFrame[chickenY][chickenX-1] > 0:
        return True
    else:
        return False

def win():
    
    """checks for win"""
    
    if chickenY == 0:
        return True
    else:
        return False

def updateVisual():
    
    """this updates the screen for crossy road for animation"""
    
    
    global ticker, increment
    ticker += increment
    
    
    gameFrame[1] = [3 * int(1 + 2*math.sin(i/5 + ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[2] = [2 * int(1 + 2*math.sin(i/10 - ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[3] = [3 * int(1 + 2*math.sin(i/6 + ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[4] = [2 * int(1 + 2.3*math.sin(i/5 - ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[5] = [3 * int(1 + 2*math.sin(i/6 + ticker)) for i in range(len(gameFrame[1]))]
    gameFrame[6] = [2 * int(1 + 3*math.sin(i/10 - ticker)) for i in range(len(gameFrame[1]))]
    
    setChickenLocation(0, 0)
    
    for q in gameFrame: 
        for i in q:
            print(density[i], end='')
        print("\n")
   
   
 
 
INSTRUCTION_DELAY = 3
print("WELCOME TO CROSSEY ROAD. ITS LIKE FROGGER BUT YOU'RE A CHICKEN LOL")
time.sleep(INSTRUCTION_DELAY)
print("PLEASE ADJUST YOUR CONSOLE SCREEN TO BE THE MAX WIDTH AND HEIGHT")
time.sleep(INSTRUCTION_DELAY)
print("YOUR 'CHICKEN' IS SIMPLY AN @ SIGN. \n BLANK SPACE IS SAFE SPACE\n ANY OTHER CHARACTER IS A 'CAR' OR 'LOG' OF SORTS")
time.sleep(INSTRUCTION_DELAY)
print("USE THE ARROWS ON THE KEYBOARD TO CONTROL THE CHICKEN AND GET IT TO THE OTHER SIDE OF THE ROAD")
time.sleep(INSTRUCTION_DELAY)


 
 
 
   
setChickenLocation(80, 7)


     
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
        
    print("why did the chicken cross the road? to win! congradulations!")
    
    time.sleep(5)