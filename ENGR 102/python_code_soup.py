x = 1 
y = 10 
z = 0 
x = y 
x += 1 
y += x 
y *= x 
z += x 
z += y 
print(z) 


print(z)
# 1 
# 26 
# 102 
# 1000000000   [Note: that’s 109] 
# 8675 