import itertools

l = [False, True]

print([list(i) for i in itertools.product(l, repeat=3)])
p = [list(i) for i in itertools.product(l, repeat=3)]


#iterates
for q in p:
    a = q[0]
    b = q[1]
    c = q[2]
    lp = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
    lo = not((not(a) and not(b) and not(c)) or (not(a) and b and not(c)) or (not(a) and b and c))
    if lp:
        print(lp, lo)
    else:
        print(lp, q, lo)
    
    

    