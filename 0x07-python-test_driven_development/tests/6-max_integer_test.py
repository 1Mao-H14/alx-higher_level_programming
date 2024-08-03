#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([0,0,0,0]), 0)
        self.assertEqual(max_integer([15.2, -1, 3.0, -3]), 15.2)
    def test_non_numbers(self):
        self.assertEqual(max_integer([15.2, -1, float('+inf'), -3]), float('+inf'))
        self.assertEqual(max_integer([15.2, -1, float('-inf'), -3]), 15.2)
        self.assertEqual(max_integer([15.2, -1, float('nan'), -3]), 15.2)
        self.assertEqual(max_integer([15.2, -1, float('nan'), -3]), 15.2)
        self.assertEqual(max_integer([0 , False , True, -3]), True)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer({0:1, 1:1, 2: 3, 3: 4}), 4)
    def test_strings(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), "d")
        self.assertRaises(TypeError, max_integer, ['a', 1, 'c', 3])
        self.assertRaises(TypeError, max_integer, [True, 'a', 'c', False])
        self.assertRaises(TypeError, max_integer, None)
