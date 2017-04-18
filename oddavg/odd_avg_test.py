import unittest
from odd_avg import Odd_Averager


class Odd_Average_Tester(unittest.TestCase):
    def test_zero(self):
        zero_list = Odd_Averager()
        self.assertEqual(zero_list.odd_average([]), 0)

    def test_even_list(self):
        even_list = Odd_Averager()
        self.assertEqual(even_list.odd_average([2, 4, 0]), 0)

    def test_normal_list(self):
        normal_list = Odd_Averager()
        self.assertEqual(normal_list.odd_average([1, 2, 4, 3,  0]), 2)

if __name__ == '__main__':
    unittest.main()
