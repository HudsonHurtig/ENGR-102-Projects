# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

dictionary = {
  "a": "4",
  "e": "3",
  "o": "0",
  "s":"5",
  "t":"7"
}



string = str(input("Enter some text:"))
t = string

for i in range(100):
    
    for key in dictionary.keys():
    
        string = string.replace(key, dictionary[key])

print(f"In leet speak, \"{t}\" is:{string}")