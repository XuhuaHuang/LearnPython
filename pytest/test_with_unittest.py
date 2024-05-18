# -*- coding: utf-8 -*-
# python -m unittest discover

from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)


    def test_always_fails(self):
        self.assertTrue(False)
