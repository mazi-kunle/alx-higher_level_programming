#!/usr/bin/python3

max_integer = __import__('6-max_integer').max_integer
import unittest

class test_max_integer(unittest.TestCase):
    def test_max(self):
        a = [0,1,2,3]
        self.assertAlmostEqual(max_integer(a), 3)

    def test_max2(self):
        a = [-1,-2,-3]
        self.assertAlmostEqual(max_integer(a), -1)

    def test_max3(self):
        a = []
        self.assertAlmostEqual(max_integer(a), None)

    def test_max4(self):
        a = [3,2,1]
        self.assertAlmostEqual(max_integer(a), 3)

    def test_max5(self):
        a = [2]
        self.assertAlmostEqual(max_integer(a), 2)

    def test_max6(self):
        a = ['a','b',1]
        self.assertRaises(TypeError, max_integer, a)
        
    def test_max7(self):
        a = [1,4,2]
        self.assertAlmostEqual(max_integer(a), 4)
