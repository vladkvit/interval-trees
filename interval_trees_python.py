import numpy as np

def intersect(int1, int2):
    if int1.right < int2.left:
        return False
    if int2.right < int1.left:
        return False
    return True


class Interval:
    def __init__(self, left, right, inclusiveL = False, inclusiveR = False):
        assert(left <= right)
        self.left = left
        self.right = right
        self.inclusiveL = inclusiveL
        self.inclusiveR = inclusiveR


intlist = []

for x in range(0, 5):
    tmpint = Interval( x, x + 3 )
    intlist.append( tmpint )

for x, y in np.ndindex(( len(intlist), len(intlist) )):
    print(x, y)
    print( intersect( intlist[x], intlist[y] ) )

