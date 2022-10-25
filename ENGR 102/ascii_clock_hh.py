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
# Assignment:   Lab 8
# Date:         10 23 22

if len(time) == 5: # output if double digit hours
    for x in range(5): # adds ascii text row by row to output
        for i in time:
            output.append(text[i][x])

    while counter <= 25: # ourpur result row by row
        if (counter+1) % 5 == 0: # prints a new line when needed
            print(output[counter], end=' ')
            print()
        else:
            if counter < 25:
                print(output[counter], end=' ')
       
        counter += 1