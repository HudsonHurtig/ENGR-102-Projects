# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

def validateBarcode(string):
       
   intStr = [int(string[i]) for i in range(0,12)]
   
   sum1 = sum(intStr[::2])
   sum2 = sum(intStr) - sum1
   num3 = sum2*3
   num4 = num3 + sum1
   num5 = num4 % 10
   num6 = 10 - num5
   
   return int(string[12]) == num6


in1 = input("Enter the name of the file:")

with open(in1) as file:
    counter = 0
    bigString = file.read()
    bigList = bigString.split("\n")
    
    for i in bigList:
        
        if validateBarcode(i):
            
            counter+=1
            f = open("valid_barcodes.txt", "a")
            f.write(i+"\n")
            f.close()
        
        #print(i, validateBarcode(i))
        
    print(" There are",counter,"valid barcodes")
    
    

