print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = not(x) or not(y) or not(z) or not(w)
                if F == 0 and x + y + z + w == 3:
                    print(x, y, z, w)
 
