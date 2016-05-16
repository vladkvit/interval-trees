import numpy as np
from collections import namedtuple

def intersect(int1, int2):
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

    #returns: -1 if point is to the left,
    #         +1 if point is to the right,
    #         0 if point is contained
    def point_location(self, point):
        if self.inclusiveL:
            less_comparator = lambda a, b: a < b
        else:
            less_comparator = lambda a, b: a <= b
        if less_comparator( point, self.left ):
            return -1
        
        if self.inclusiveR:
            greater_comparator = lambda a, b: a > b
        else:
            greater_comparator = lambda a, b: a >= b
        if greater_comparator( point, self.right ):
            return 1

        return 0

class IntTreeNode:
    def __init__(self,data,point):
        self.left = None
        self.right = None
        self.data = [data]
        self.point = point

class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, int1 ):
        if self.root == None:
            self.root = IntTreeNode( int1, (int1.left+int1.right)/2)
        else:
            parent = None
            node = self.root
            while node != None:
                parent = node
                direction = int1.point_location( node.point )
                if direction < 0:
                    node = node.right
                elif direction > 0:
                    node = node.left
                else:
                    #insert into node
                    node.data.append( int1 )
                    break
            if node == None:
                self.insert_new_node(parent, IntTreeNode( int1, (int1.left+int1.right)/2))

    def insert_recursive_helper(self, int1, node):
        if node == None:
            return 0
        direction = int1.point_location( node.point )
        if direction < 0:
            result = self.insert_recursive_helper(self, int1, node.left)
        elif direction > 0:
            result = self.insert_recursive_helper(self, int1, node.right)
        else:
            node.data.append( int1 )

        if result == 0:
            self.insert_new_node( parent, IntTreeNode( int1, (int1.left+int1.right)/2))

        return 1

    def insert_recursive(self, int1):
        result = self.insert_recursive_helper( int1, self.root )
        if result == 0:
            self.root = IntTreeNode( int1, (int1.left+int1.right)/2)

    def insert_new_node( self, parent, newnode ):
        assert( parent != None )
        pass

    def queryinterval(self, int1):
        node = self.root
        while node != None:
            direction = int1.point_location( node.point )
            if direction < 0:
                node = node.right
            elif direction > 0:
                node = node.left
            else:
                break
        return node

    def query(self, position):
        pos = Interval( position, position, True, True )
        return self.queryinterval(pos)

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
