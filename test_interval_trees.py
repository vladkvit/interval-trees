import unittest
import interval_trees_python as itv

class Test_test1(unittest.TestCase):
    def test_tree_none(self):
        tree = itv.IntervalTree()
        testinterval = itv.Interval(1, 2)
        self.assertTrue( tree.queryinterval(testinterval) == None)

    def test_tree_two(self):
        a = itv.Interval(1, 2)
        b = itv.Interval(2,3)
        tree = itv.IntervalTree()
        tree.insert( a )
        tree.insert( b )
        self.assertTrue( tree.query( 1 ) == None )
        self.assertFalse( tree.query( 1.5 ) == None )
        self.assertFalse( tree.query( 1.5 ) == None )

    def test_tree_three(self):
        a = itv.Interval(1, 2)
        b = itv.Interval(2,3)
        c = itv.Interval(2,4)
        tree = itv.IntervalTree()
        tree.insert( a )
        tree.insert( b )
        tree.insert( c )


if __name__ == '__main__':
    unittest.main()
