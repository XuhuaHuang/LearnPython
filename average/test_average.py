# -*- coding: utf-8 -*-

import unittest

from average import average


class TestStatisticalFunctions(unittest.TestCase):
    """Tests for `average.py`.

    Args:
        unittest (_type_): Test case class.
    """

    def test_average(self):
        """Test the average function from the average module.
        """
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


if __name__ == '__main__':
    unittest.main()  # Calling from the command line invokes all tests
