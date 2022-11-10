# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

with open("WeatherDataCLL.csv") as file:
    counter = 0
    bigString = file.read()
    
    bigList = bigString.split("\n")
    
    biggerList = [i.split(",") for i in bigList]
    biggerList.pop() # get rid of last element
    
    dates = [i[0] for i in biggerList]
    avgWindSpeed = [i[1] for i in biggerList]
    Precipritation = [i[2] for i in biggerList]   
    avgTemp = [i[3] for i in biggerList]   
    maxTemp = [i[4] for i in biggerList]   
    minTemp = [i[5] for i in biggerList]  
    
    
    print(maxTemp[0])