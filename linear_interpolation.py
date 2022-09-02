# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Hudson Hurtig
#               Avi Punjabi
#               Brian Tran
#               MJ Murray
#               Gabriel Isaac
# Section:      505
# Assignment:   Lab 2
# Date:         9-2-2022

from math import *
#part 1
time1 = 25 

print("Part 1:")
print("For t =",time1,"minutes, the position p =",round(((time1*((23026-2026)/45)) - (2640+(2/3))),1),"kilometers")

#part 2
time2 = 300

print("Part 2:")
print("For t = ",time2," minutes, the position p =",((time2*((23026-2026)/45)) - (2640+(2/3))) % (2*pi*6745),"kilometers")