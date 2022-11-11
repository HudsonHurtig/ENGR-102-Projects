# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

def normalizeOperation(q, num, a):
    
    value = int(q[6:])
    
    if q[5] == "+":
        
        num += value
        if a:
            f = open("coins.txt", "a")
            f.write(str(value)+"\n")
            f.close()
        
    else:
        
        num -= value
        
        if a:
            f = open("coins.txt", "a")
            f.write("-"+str(value)+"\n")
            f.close()
    
    return num

with open("game.txt") as file:
    counter = 0
    bigString = file.read()
    bigList = bigString.split("\n")
    #print(bigList)
    
    n = 0
    
    coins = 0
    
    while n != len(bigList)-1:
        
        instruction = bigList[n]
        
        if instruction[0] == 'j':
            
            n = normalizeOperation(instruction, n, False)
        
        elif instruction[0] == 'c':
            
            coins = normalizeOperation(instruction, coins, True)
            
            n += 1
            
        else:
            
            n += 1
        
       
    print("Total coins collected:", coins)
        
    