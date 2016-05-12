import numpy as np

def intersect(int1, int2):
    #less_comparator
    if int1.inclusiveR and int2.inclusiveL:
        less_comparator = lambda a, b: a < b
    else:
        less_comparator = lambda a, b: a <= b
    if less_comparator( int1.right, int2.left):
        return False

    if int1.inclusiveL and int2.inclusiveR:
        less_comparator = lambda a, b: a < b
    else:
        less_comparator = lambda a, b: a <= b

    if less_comparator( int2.right, int1.left):
        return False

    return True


class Interval:
    def __init__(self, left, right, inclusiveL = False, inclusiveR = False):
        assert(left <= right)
        self.left = left
        self.right = right
        self.inclusiveL = inclusiveL
        self.inclusiveR = inclusiveR

    def prettyprint(self, endx="\n"):
        print(self.left, self.right, \
            "T" if self.inclusiveL else "F", \
            "T" if self.inclusiveL else "F", end=endx)

def debuggy():
    intlist = []

    for x in range(0, 5):
        tmpint = Interval( x, x + 3 )
        intlist.append( tmpint )

    for x in range(0, len(intlist)):
        print( "[ ", end="" )

        for y in range(0, len(intlist)):
            letter = "T " if intersect( intlist[x], intlist[y] ) else "F "
            print( letter, end="" )
        print( "]")
