import unittest
import interval_trees_python as itv

class Test_test1(unittest.TestCase):
    def test_A(self):
        a = itv.Interval(1, 2)
        b = itv.Interval(2,3)
        self.assertFalse( itv.intersect(a,b) )

    def test_B(self):
        a = itv.Interval(1,2, False, False)
        b = itv.Interval(2,3, False, False)
        self.assertFalse( itv.intersect(a,b) )

    def test_C(self):
        a = itv.Interval(1,2, True, False)
        b = itv.Interval(2,3, False, True)
        self.assertFalse( itv.intersect(a,b) )

    def test_D(self):
        a = itv.Interval(1,2, False, True)
        b = itv.Interval(2,3, False, False)
        self.assertFalse( itv.intersect(a,b) )

    def test_E(self):
        a = itv.Interval(1,2, False, True)
        b = itv.Interval(2,3, True, False)
        self.assertTrue( itv.intersect(a,b) )

    def test_F(self):
        a = itv.Interval(1,2, True, True)
        b = itv.Interval(1,2, True, True)
        self.assertTrue( itv.intersect(a,b) )

        a = itv.Interval(1,2, False, False)
        b = itv.Interval(1,2, False, False)
        self.assertTrue( itv.intersect(a,b) )

    def test_G(self):
        a = itv.Interval(1,2, True, True)
        b = itv.Interval(3,4, True, True)
        self.assertFalse( itv.intersect(a,b) )

        a = itv.Interval(1,2, False, False)
        b = itv.Interval(3,4, False, False)
        self.assertFalse( itv.intersect(a,b) )

    def test_moreA(self):
        intlist = []

        for x in range(0, 5):
            tmpint = itv.Interval( x, x + 3 )
            intlist.append( tmpint )
        


if __name__ == '__main__':
    unittest.main()
