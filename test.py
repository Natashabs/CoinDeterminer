#!/usr/bin/env python

__author__ = 'natasha'

import unittest
from coin import CoinDeterminer


class MyTestCase(unittest.TestCase):

    def test_example_input(self):
        self.assertEqual(CoinDeterminer(6), 2, "Wrong change for 6")
        self.assertEqual(CoinDeterminer(16), 2, "Wrong change for 16")
        self.assertEqual(CoinDeterminer(23), 3, "Wrong change for 23")

    def test_boundaries(self):
        self.assertEqual(CoinDeterminer(1), 1, "Wrong change for 1")
        self.assertEqual(CoinDeterminer(250), 24, "Wrong change for 250")

    def test_big_number(self):
        self.assertEqual(CoinDeterminer(99999), 9091, "Wrong change for 99999")


if __name__ == '__main__':
    unittest.main()
