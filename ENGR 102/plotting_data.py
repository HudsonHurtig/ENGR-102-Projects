# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      505
# Assignment:   lab 12
# Date:         11-17-22
#


# this is some comment


import numpy as np
from matplotlib import pyplot as plt
data  = []
with open("WeatherDataCLL.csv") as file:
    plt.title("max temp(g) / average wind speed(r) VS Days in File") 
    plt.xlabel("days") 
    plt.ylabel("max temp / average wind speed") 
    counter = 0
    bigString = file.read()
    bigList = bigString.split("\n")
    print(bigList[0])
    bigList = bigList[1:len(bigList)]
    biggerList = [i.split(",") for i in bigList]
    for i in biggerList:
        i[1:] = map(float, i[1:])
    biggerList.pop()
    data = biggerList
        
        # print(i,len(biggerList[i]))
    plt.plot(range(len(biggerList)),[i[1] for i in biggerList])
    plt.plot(range(len(biggerList)),[i[4] for i in biggerList])
        
        
print(biggerList[0])
plt.show()
        
plt.title("max temp(g) / average wind speed(r) VS Days in File") 
plt.xlabel("inches of rain") 
plt.ylabel("number of days") 

hist = [data[i][4] for i in range(len(data))]

plt.hist(hist)
plt.show()

plt.title("AVG wind speed VS Min tempurature") 
plt.xlabel("AVG wind speed") 
plt.ylabel("tempurature") 

for i in range(len(data)):
    plt.plot(data[i][1],data[i][-1],"bo")

plt.show()


months = [i[0].split("/") for i in data]
    
for i in range(len(data)):
    
    data[i][0] = int(months[i][0])
    
print(data[0])

Jdat = [i[3] for i in data if i[0] == 1]
Fdat = [i[3] for i in data if i[0] == 2]
Mdat = [i[3] for i in data if i[0] == 3]
Adat = [i[3] for i in data if i[0] == 4]
Madat = [i[3] for i in data if i[0] == 5]
Judat = [i[3] for i in data if i[0] == 6]
Juldat = [i[3] for i in data if i[0] == 7]
Audat = [i[3] for i in data if i[0] == 8]
Sdat = [i[3] for i in data if i[0] == 9]
Odat = [i[3] for i in data if i[0] == 10]
Ndat = [i[3] for i in data if i[0] == 11]
Ddat = [i[3] for i in data if i[0] == 12]

plt.title("Box plot for avg temp") 
plt.xlabel("month") 
plt.ylabel("tempurature") 

plt.boxplot([Jdat,Fdat,Mdat,Adat,Madat,Judat,Juldat,Audat,Sdat,Odat,Ndat,Ddat])

plt.show()

print(Ddat)