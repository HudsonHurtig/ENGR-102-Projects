
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Hudson Hurtig
# Section:      575
# Assignment:   lab 6
# Date:         9-22-22

#silly whittle comment

import math

a = (str(input("Enter the elements for vector A:"))).split(" ")
b = (str(input("Enter the elements for vector B:"))).split(" ")
 
a = [eval(i) for i in a]
b = [eval(i) for i in b]


         
print(f"The magnitude of vector A is {(math.sqrt(sum([a[i] * a[i] for i in range(len(a))]))):.5f}")
print(f"The magnitude of vector B is {(math.sqrt(sum([b[i] * b[i] for i in range(len(b))]))):.5f}")
print(f"A + B is {[float(a[i] + b[i]) for i in range(len(a))]}")
print(f"A - B is {[float(a[i] - b[i]) for i in range(len(a))]}")
print(f"The dot product is { sum([a[i] * b[i] for i in range(len(a))]):.2f}")