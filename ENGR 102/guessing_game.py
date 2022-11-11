# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment
import random

def get_input(b):
    #comment
    if b:
        q = int(input("Try again: "))
    else:
        q = int(input("What is your guess? "))
    return q

def isH(b):
    #comment
    if b:
        print("Too high!")
    else:
        print("Too low!")
        
    
    
print("Guess the secret number! Hint: it's an integer between 1 and 100...")

number =26

tries = 0
va = True
b = False
while va:
    
    
    
    try:
    
        in1 = get_input(b)
        tries += 1
        b = False
        
        if number < in1:
            
            isH(True)
            
        elif number > in1:
            
            isH(False)
            
        else:
            
            print(f"You guessed it! It took you {tries} guesses.")
            va = False

    
    except:
        b = True
        print("Bad input", end="! ")
        
        