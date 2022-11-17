# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      505
# Assignment:   lab 12
# Date:         11-17-22
#


# this is some comment

import numpy as np
from matplotlib import pyplot as plt
v = np.array([[0],[1]])

M = np.array([[1.01, 0.09], [-0.09, 1.01]])

ptArray = []

plt.title("Spiral generated via matrix multiplication") 
plt.xlabel("x value") 
plt.ylabel("y value") 


for i in range(200):
    v = M@v
    plt.plot(v[0],v[1],"o") 
plt.show()