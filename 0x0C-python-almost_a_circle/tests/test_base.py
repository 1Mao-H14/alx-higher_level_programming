#!/usr/bin/python3

""""a module which containes tests of the base class"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_class_creation(self):
        # simple tests
        a = Base(None)
        self.assertEqual(a.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)
        c = Base(89)
        self.assertEqual(c.id, 89)
