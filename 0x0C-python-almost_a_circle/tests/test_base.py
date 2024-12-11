#!/usr/bin/python3

""""a module which containes tests of the base class"""
import models.base
import unittest


class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_class_creation(self):
        # simple tests
        a = Base(None)
        self.assertEqual(a.id, 1)

    def test_auto_increment(self):
        b = Base(None)
        c = Base(None)
        self.assertEqual(b.id + 1, c.id)

    def test_saving_id(self):
        d = Base(89)
        self.assertEqual(d.id, 89)
