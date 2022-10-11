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
# Assignment:   Lab 7
# Date:         10 07 22

black = chr(9679) #black tile (assuming white background)
white = chr(9675) #white tile (assuming white background)

#writes out each row, including the one labeling each column
row9 = ["9", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row8 = ["8", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row7 = ["7", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row6 = ["6", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row5 = ["5", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row4 = ["4", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row3 = ["3", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row2 = ["2", ".", ".", ".", ".", ".", ".", ".", ".", "."]
row1 = ["1", ".", ".", ".", ".", ".", ".", ".", ".", "."]
cols = [' ', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

board = [row9, row8, row7, row6, row5, row4, row3, row2, row1, cols] #arranges each row

turn = 1 #initializes the turn count at 1

while 1 == 1: #loops forever, is only broken when user enters 'stop'

    for i in range(len(board)): #prints the board
        print(board[i], sep='\n')

    coords = input("Please enter the coordinates of where you would like to place a stone (seperated by a space), or enter \'stop\' to end the game: ")

    if coords != 'stop': #if the user doesn't enter stop, the program continues

        coords = coords.split() #splits the coordinate input into a list storing each input as a separate element

        for i in range(len(coords)): #makes each element an integer
            coords[i] = int(coords[i])

        while (coords[0] < 1 or coords[0] > 9) or (coords[1] < 1 or coords[1] > 9): #loops until integers are between 1 and 9

            print("Invalid inputs, please enter two integers from 1 to 9.")
            coords = input("Please enter the coordinates of where you would like to place a stone (seperated by a space): ") #already ruled out that user wants to stop, so we can ask for coords only
            coords = coords.split()

            for i in range(len(coords)):
                coords[i] = int(coords[i])

        if turn % 2 == 1: #if the turn count is odd, use the black tile
            tile = black
        else: #if the turn count is even, use the white tile
            tile = white

        if board[9-coords[1]][coords[0]] == ".": #checks if a tile has already been placed in this spot, if it hasn't then replace the period with the tile
            board[9-coords[1]] = board[9-coords[1]][:coords[0]] + [tile] + board[9-coords[1]][coords[0] + 1:]
            turn += 1
        else: #if spot is already taken, loop back without changing the turn count
            print("This spot is already taken, please try again.")
            
    else: #if the user does enter stop, break the loop
        break

print("Here is the final board, thanks for playing!")
for i in range(len(board)): #prints the board one last time
        print(board[i], sep='\n')