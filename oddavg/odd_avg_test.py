import unittest
from odd_avg import OddAverager


class OddAverageTester(unittest.TestCase):
    def test_zero(self):
        zero_list = OddAverager()
        self.assertEqual(zero_list.odd_average([]), 0)

    def test_even_list(self):
        even_list = OddAverager()
        self.assertEqual(even_list.odd_average([2, 4, 0]), 0)

    def test_normal_list(self):
        normal_list = OddAverager()
        self.assertEqual(normal_list.odd_average([1, 2, 4, 3,  0]), 2)

if __name__ == '__main__':
    unittest.main()
