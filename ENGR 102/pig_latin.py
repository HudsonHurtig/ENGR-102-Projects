# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


vowels = ["a","A","e","E","i","I","o","O","u","U","y","y"]
ay = 'ay'
yay = "yay"
string = str(input("Enter word(s) to convert to Pig Latin:"))

w = string.split(" ")
ad = ''
for i in range(len(w)):
    ad = ''
    if w[i][0] in vowels:
        w[i] = w[i] + (yay)
        continue
    for q in w[i]:
        if q not in vowels: 
            ad = ad + q
        else:
            
            w[i] = w[i].replace(ad,'',1) + ad + ay
            
            break
            
    
    


print(f"In Pig Latin, \"{string}\" is: {' '.join(w)}")
            
    
         
        