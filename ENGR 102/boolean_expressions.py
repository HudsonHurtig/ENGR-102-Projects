# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Hudson Hurtig
#               Avi Punjabi
#               Brian Tran
#               MJ Murray
#               Gabriel Isaac
# Section:      575
# Assignment:   Lab #4
# Date:         9-15-2022

#whittle comment


############ Part A ############
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")

bols = [a,b,c]

lT = ["True", "T", "t"]
lF = ["False", "F", "f"]

for q in range(len(bols)):
    if bols[q] in lT:
        bols[q] = True
    elif bols[q] in lF:
        bols[q] = False


############ Part B ############
print("a and b and c:",(bols[0] and bols[1] and bols[2]))


print("a or b or c:",(bols[0] or bols[1] or bols[2]))

############ Part C ############

print("XOR:", (not(bols[0] == bols[1]) or (bols[0] != bols[1]))) 

a = bols[0]
b = bols[1]
c = bols[2]

print("Odd number:",(a and b and c) or (a and not(b) and not(c)) or (not(a) and b and not(c)) or (not(a) and not(b) and c))

############ Part D ############

print("Complex 1:",(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
print("Complex 2:", (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b 
and c) or (a and ((b and not c) or (not b)))))

print("Simple 1", not(not(a) and b and c or a and b and not(c) or a and b and c))
print("Simple 2", not((not(a) and not(b) and not(c)) or (not(a) and b and not(c)) or (not(a) and b and c)))