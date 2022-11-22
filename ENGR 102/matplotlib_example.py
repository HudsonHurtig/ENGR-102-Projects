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
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100) # creates an array of 100 evenly spaced x-values from -2 to 2

def parabola(f): # defines a function that takes in the focal length and outputs its respective parabola
    y = (x ** 2) / (4 * f)
    plt.plot(x,y,label=f'f={f}',linewidth=f)

#output both parabolas
parabola(2)
parabola(6)

#label title, legend, and axes
plt.title('Parabola plots with varying focal length')
plt.legend(loc='lower left')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

x = np.linspace(-4,4,25) # creates an array of 25 evenly spaced x-values from -4 to 4
y = 2 * x ** 3 + 3 * x ** 2 - 11 * x - 6 # defines y as a function of x

plt.plot(x,y,marker='*',linewidth=0) # plots the graph

#sets title and labels
plt.title('Plot of cubic polynomial')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()

fig, ax = plt.subplots(2, 1, sharex=True) # creates 2 subplots that share an x-axis

x = np.linspace(-2 * np.pi, 2 * np.pi, 100) # creates an array of 100 evenly spaced x-values from -2pi to 2pi

y1 = np.cos(x)
y2 = np.sin(x)

#first subplot
ax[0].plot(x,y1, color=('red'), label='cos(x)')
ax[0].set_ylabel('y=cos(x)')
ax[0].legend(loc='lower right')

#second subplot
ax[1].plot(x,y2, color=('blue'), label='sin(x)')
ax[1].set_ylabel('y=sin(x)')
ax[1].legend(loc='upper right')

#title and x-label
ax[1].set_xlabel('x')
ax[0].set_title('Plot of cos(x) and sin(x)')

#grids
ax[0].grid(True)
ax[1].grid(True)

plt.show()