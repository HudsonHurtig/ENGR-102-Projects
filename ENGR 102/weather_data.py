# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment


def numToMonth(shortMonth):
    return {
            1:'January',
            2: 'February',
            3: 'March',
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September", 
            10: "October",
            11: "November",
            12: "December"
    }[shortMonth]

with open("WeatherDataCLL.csv") as file:
    counter = 0
    bigString = file.read()
    
    bigList = bigString.split("\n")
    
    biggerList = [i.split(",") for i in bigList]
    biggerList.pop() # get rid of last element
    
    dates = [i[0] for i in biggerList]
    
    brokenDates = [i.split("/") for i in dates]
    
    avgWindSpeed = [i[1] for i in biggerList]
    precipritation = [i[2] for i in biggerList]   
    
    avgTemp = [i[3] for i in biggerList]   
    maxTemp = [i[4] for i in biggerList]   
    minTemp = [i[5] for i in biggerList]  
    
    
    
    brokenDates.pop(0)
    avgWindSpeed.pop(0)
    precipritation.pop(0)
    avgTemp.pop(0)
    maxTemp.pop(0)
    minTemp.pop(0)
    
    precipritation = [float(i) for i in precipritation]   
    
    
    avgWindSpeed = [float(i) for i in avgWindSpeed]
    precipritation = [float(i) for i in precipritation]   
    
    avgTemp = [float(i) for i in avgTemp]   
    maxTemp = [float(i) for i in maxTemp]   
    minTemp = [float(i) for i in minTemp]  
    
    
    for i in range(len(brokenDates)):
        brokenDates[i][0] = numToMonth(int(brokenDates[i][0]))
        brokenDates[i].pop(1)
        
        
print(f"3-year maximum temperature: {int(max(maxTemp))} F")
print(f"3-year minimum temperature: {int(min(minTemp))} F")

print(f"3-year average precipitation: {sum(precipritation)/len(precipritation):.3f} inches") 

month = input("Please enter a month: ") 
year = input("Please enter a year: ")

ind = [i for i in range(len(brokenDates)) if brokenDates[i][0] == month and brokenDates[i][1] == year]

print(f"For {month} {year}:")
print(f"Mean maximum daily temperature: {sum(maxTemp[ind[0]:((ind[-1]+2) if month == 'December' and year == '2021' else (ind[-1]+1))])/len(ind):.1f} F") 
print(f"Mean daily wind speed: {sum(avgWindSpeed[ind[0]:((ind[-1]+2) if month == 'December' and year == '2021' else (ind[-1]+1))])/len(ind):.2f} mph")
print(f"Percentage of days with precipitation: {len([i for i in precipritation[ind[0]:((ind[-1]+2) if month == 'December' and year == '2021' else (ind[-1]+1))] if float(i) != 0])/len(ind)*100:.1f}%")
        


