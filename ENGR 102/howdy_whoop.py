# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

in1 = int(input("Enter an integer:"))  
in2 = int(input("Enter another integer:")) 

n = 1
while n <= 100:
    if n % in1 == 0 and n % in2 ==0:
        print("Howdy Whoop")
    elif n % in1 == 0:
        print("Howdy")
    elif n % in2 == 0:
        print("Whoop")
    else:
        print(n)
    
    n+=1
