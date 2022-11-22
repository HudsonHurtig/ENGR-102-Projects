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
# Assignment:   Lab 12
# Date:         11 17 22

# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 

import numpy as np

A = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]]) # Defines matrix A
B = np.array([[0,1],[2,3],[4,5],[6,7]]) # Defines matrix B
C = np.array([[0,1,2],[3,4,5]]) # Defines matrix C
D = np.matmul(np.matmul(A,B),C) # Defines matrix D as the matrix product of A, B, and C
Dt = D.transpose() # Stores the transpose of D
E = np.sqrt(D) / 2 # Calculates and stores matrix E

#Outputs
print('A =', A)
print('')
print('B =', B)
print('')
print('C =', C)
print('')
print('D =', D)
print('')
print('D^T =', Dt)
print('')
print('E =', E)