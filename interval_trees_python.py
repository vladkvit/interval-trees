import numpy as np
from collections import namedtuple
from copy import deepcopy

#returns 0 if int1 and int2 intersect anywhere
#returns -1 if int1 is to the left of int2
#returns +1 if int2 is to the right of int2
def intersect(int1, int2):
    #TODO handle points with one inclusive one exclusive
    if int1.inclusiveR and int2.inclusiveL:
        less_comparator = lambda a, b: a < b
    else:
        less_comparator = lambda a, b: a <= b
    if less_comparator( int1.right, int2.left):
        return -1

    if int1.inclusiveL and int2.inclusiveR:
        less_comparator = lambda a, b: a < b
    else:
        less_comparator = lambda a, b: a <= b

    if less_comparator( int2.right, int1.left):
        return 1

    return 0

def intersectB(int1,int2):
    return intersect(int1,int2) == 0

#returns the interval that is leftmost.
#returns int1 if both intervals start at the same point
def leftmost(int1, int2):
    if int1.left < int2.left:
        return int1

    elif int2.left < int1.left:
        return int2

    elif int2.inclusiveL and int1.inclusiveL == False:
        return int2

    return int1

#returns the interval that is rightmost.
#returns int1 if both intervals start at the same point
def rightmost(int1, int2):
    if int1.left > int2.left:
        return int1

    elif int2.left > int1.left:
        return int2

    elif int2.inclusiveR and int1.inclusiveR == False:
        return int2

    return int1

def int_union(int1, int2):
    assert( intersect(int1, int2) == 0 )
    int3 = Interval( 0,0)

    lower = leftmost(int1,int2)
    int3.left = lower.left
    int3.inclusiveL = lower.inclusiveL

    upper = rightmost(int1,int2)
    int3.right = upper.right
    int3.inclusiveR = upper.inclusiveR
    return int3

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
        test_int = Interval(point, point, True, True)
        return intersect(test_int,self)

class IntTreeNode:
    def __init__(self,data,point):
        self.left = None
        self.right = None
        self.data = [data]
        self.point = point
        self.range = data

    def add_data(self, newint):
        assert(newint.point_location( self.point ) == 0)
        self.data.append(newint)
        self.range = int_union( self.range, newint )

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
                    node.add_data( int1 )
                    break
            if node == None:
                self.insert_new_node(parent, IntTreeNode( int1, (int1.left+int1.right)/2),
                                     direction * -1 )

    def insert_recursive_helper(self, int1, node):
        if node == None:
            return 0
        direction = int1.point_location( node.point )
        if direction < 0:
            result = self.insert_recursive_helper(self, int1, node.right)
        elif direction > 0:
            result = self.insert_recursive_helper(self, int1, node.left)
        else:
            node.add_data( int1 )

        if result == 0:
            self.insert_new_node( self, IntTreeNode( int1, (int1.left+int1.right)/2),
                                  direction * -1 )

        return 1

    def insert_recursive(self, int1):
        result = self.insert_recursive_helper( int1, self.root )
        if result == 0:
            self.root = IntTreeNode( int1, (int1.left+int1.right)/2)

    def insert_new_node( self, parent, newnode, direction ):
        assert( parent != None )
        if direction < 0:
            parent.left = newnode
        elif direction > 0:
            parent.right = newnode
        else:
            assert( False )

    #answers "what lies in this interval"
    def queryinterval(self, int1):
        traverse_list = []
        node = self.root
        while node != None:
            if intersect( node.range, int1 ) == 0:
                traverse_list.append( node.data )

            direction = int1.point_location( node.point )
            if direction < 0:
                node = node.right
            elif direction > 0:
                node = node.left
            else:
                break
        
        return traverse_list

    #returns whether point position is within the interval tree or not
    def query(self, position):
        pos = Interval( position, position, True, True )
        return self.queryinterval(pos)

