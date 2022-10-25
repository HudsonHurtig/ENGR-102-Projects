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

time = input("Enter the time: ") # stores the user's input
print("")

text = { # dictionary mapping each digit (and colon) to its ascii counterpart
    '1' : [ # 1
        ' 1 ', 
        '11 ', 
        ' 1 ', 
        ' 1 ', 
        '111'
        ],
    '2' : [ # 2
        '222', 
        '  2', 
        '222', 
        '2  ', 
        '222'
        ],
    '3' : [ # 3
        '333', 
        '  3', 
        '333', 
        '  3', 
        '333'
        ],
    '4' : [ # 4
        '4 4', 
        '4 4', 
        '444', 
        '  4', 
        '  4'
        ],
    '5' : [ # 5
        '555', 
        '5  ', 
        '555', 
        '  5', 
        '555'
        ],
    '6' : [ # 6
        '666', 
        '6  ', 
        '666', 
        '6 6', 
        '666'
        ],
    '7' : [ # 7
        '777', 
        '  7', 
        '  7', 
        '  7', 
        '  7'
        ],
    '8' : [ # 8
        '888', 
        '8 8', 
        '888', 
        '8 8', 
        '888'
        ],
    '9' : [ # 9
        '999', 
        '9 9', 
        '999', 
        '  9', 
        '999'
        ],
    '0' : [ # 0
        '000', 
        '0 0', 
        '0 0', 
        '0 0', 
        '000'
        ],
    ':' : [ # :
        ' ', 
        ':', 
        ' ', 
        ':', 
        ' '
        ]
}

output = [] # stores the output

counter = 0 # stores a counter for the output

while 1 == 1: # this loop ensures that the input is valid
    if time[1] == ':' and len(time[2:]) == 2: # colon in the right spot in the form x:xx
        if time[0].isdigit() and time[2:].isdigit(): # digits are integers
            if int(time[2:]) <= 59: # minutes arent 60 or more
                break
            else:
                print("Invalid input, please try again")
                time = input("Enter the time: ")
                continue
        else:
            print("Invalid input, please try again")
            time = input("Enter the time: ")
            continue
    elif time[2] == ':' and len(time[3:]) == 2: # colon in the right spot in the form xx:xx
        if time[0] == '0' and time[1] != '0': # fix leading zero
            newTime = time[1:]
            time = newTime
            continue

        if time[:2].isdigit() and time[3:].isdigit(): # digits are integers
            if int(time[3:]) <= 59: # minutes arent 60 or more
                if int(time[:2]) <= 12: # normal time
                    if int(time[0:2]) == 0: # fix double zero
                        newTime = "12" + time[2:]
                        time = newTime
                    break
                elif int(time[:2]) <= 23: # fix military time
                    newTime = str(int(time[:2]) - 12) + time[2:]
                    time = newTime
                    break
                else:
                    print("Invalid input, please try again")
                    time = input("Enter the time: ")
                    continue
            else:
                print("Invalid input, please try again")
                time = input("Enter the time: ")
                continue
        else:
            print("Invalid input, please try again")
            time = input("Enter the time: ")
            continue
    else:
        print("Invalid input, please try again")
        time = input("Enter the time: ")
        continue

if len(time) == 4: # output if single digit hours
    for x in range(5): # adds ascii text row by row to output
        for i in time:
            output.append(text[i][x])

    while counter <= 20: # output result row by row
        if (counter+1) % 4 == 0: # prints a new line when needed
            print(output[counter], end=' ')
            print()
        else:
            if counter < 20:
                print(output[counter], end=' ')
        
        counter += 1
elif len(time) == 5: # output if double digit hours
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