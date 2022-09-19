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
# Assignment:   Lab 4.14.1
# Date:         09 15 22

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

if A != 0 and B != 0 and C != 0: #if none of them are zero then we display each coefficient in some way

    if A == 1:
        A = ""
    elif A == -1: 
        A = "- "
    elif A < 0:
        A = "- " + str(-A)
    elif A > 0:
        A = str(A)

    if B == 1:
        B = "+ "
    elif B == -1:
        B = "- "
    elif B < 0:
        B = "- " + str(-B)
    elif B > 0:
        B = "+ " + str(B)

    if C == 1:
        C = "+ 1"
    elif C == -1: 
        C = "- 1"
    elif C < 0:
        C = "- " + str(-C)
    elif C > 0:
        C = "+ " + str(C)

    print(f'The quadratic equation is {A}x^2 {B}x {C} = 0')

elif ((A == 0 or B == 0) and C != 0) or ((A == 0 or C == 0) and B != 0) or (A != 0 and (B == 0 or C == 0)): #if at least one but not all three are zero then we don't include some of the terms
    
    if A == 0:
        
        if B == 1:
            B = ""
        elif B == -1:
            B = "- "
        elif B < 0:
            B = "- " + str(-B)
        elif B > 0:
            B = str(B)

        if C == 1:
            C = "+ 1"
        elif C == -1: 
            C = "- 1"
        elif C < 0:
            C = "- " + str(-C)
        elif C > 0:
            C = "+ " + str(C)

        if B == 0: #equation would have form C = 0 but C cannot be 0
            print("Invalid equation!")
        elif C == 0:
            print(f'The equation is {B}x = 0')
        else:
            print(f'The quadratic equation is {B}x {C} = 0')

    elif B == 0:

        if A == 1:
            A = ""
        elif A == -1: 
            A = "- "
        elif A < 0:
            A = "- " + str(-A)
        elif A > 0:
            A = str(A)

        if C == 1:
            C = "+ 1"
        elif C == -1: 
            C = "- 1"
        elif C < 0:
            C = "- " + str(-C)
        elif C > 0:
            C = "+ " + str(C)

        if C == 0:
            print(f'The quadratic equation is {A}x^2 = 0')
        else:
            print(f'The quadratic equation is {A}x^2 {C} = 0')

    elif C == 0:

        if A == 1:
            A = ""
        elif A == -1: 
            A = "- "
        elif A < 0:
            A = "- " + str(-A)
        elif A > 0:
            A = str(A)

        if B == 1:
            B = "+ "
        elif B == -1:
            B = "- "
        elif B < 0:
            B = "- " + str(-B)
        elif B > 0:
            B = "+ " + str(B)

        print(f'The quadratic equation is {A}x^2 {B}x = 0')  

else: #if all of them are zero then the equation is just 0 = 0
    print("The equation is 0 = 0")