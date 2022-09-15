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
        
print(bols)

print("a and b and c:",(bols[0] and bols[1] and bols[2]))

print("a and b and c:",(bols[0] or bols[1] or bols[2]))

print("XOR:", (not(bols[0] == bols[1]) or (bols[0] != bols[1])))
