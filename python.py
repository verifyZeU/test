print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = not(x) or not(y) or not(z) or not(w)
                if F == 0 and x + y + z + w == 3:
                    print(x, y, z, w)
 
  #x y z w
#  0 1 1 1
#  1 0 1 1    not(x) and not(y) and not(z) and not(w)
#  1 1 0 1
#  1 1 1 0


#(w <= y) == (x and z)