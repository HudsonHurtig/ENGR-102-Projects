# -*- coding: utf-8 -*-
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Avi Punjabi
#               MJ Murray
#               Hudson Hurtig
#               Gabriel Isaac
#               Brian Tran
# Section:      575
# Assignment:   Lab 6.12.1
# Date:         09 27 22


import math 

gold_foil = 0

'''((s_area * ((side_length * layers) **2)) + (3*(layers)*(layers+1))*side_length**2)/2'''

#Looking for surface area to cover triangular pyramid

while gold_foil <= 0:
   side_length = float(input("Enter the side length in meters: \n"))
   layers = float(input("Enter the number of layers: \n"))
   tri_top = ((math.sqrt(3)/4) * side_length**2) 
   tri_sides = 3 * ((layers)*(layers+1))
   tri_top *= layers ** 2
   tri_sides *= side_length**2
   tri_sides = tri_sides / 2
   gold_foil = tri_top + tri_sides
   if gold_foil > 0:
       gold_foil = round(gold_foil, 2)
       print(f'You need {gold_foil} m^2 of gold foil to cover the pyramid')
   else: 
       print("Error, Please use a different value.")