import unittest
from problem1 import *
from itertools import chain


class TestProblem1(unittest.TestCase):
    """
    Test problem 1 functions.
    """
    def test_delta_set(self):
        x_prime = 0b1011
        m = 2**4
        x_star = [0b1011, 0b1010, 0b1001, 0b1000,
                  0b1111, 0b1110, 0b1101, 0b1100,
                  0b0011, 0b0010, 0b0001, 0b0000,
                  0b0111, 0b0110, 0b0101, 0b0100]
        expected_delta = set(zip(range(m), x_star))
        self.assertEqual(expected_delta, delta_set(x_prime, m))


    def test_table_ND(self):
        """
        We are using Stinson Example 4.3 to test this function.
        """
        s_box = [0xE, 0x4, 0xD, 0x1,
                 0x2, 0xF, 0xB, 0x8,
                 0x3, 0xA, 0x6, 0xC,
                 0x5, 0x9, 0x0, 0x7]
        # checking that the only values in the table are the same
        possible_values = set([0, 2, 4, 6, 8, 16])
        table = table_ND(s_box)
        values_in_table = set(chain.from_iterable(table))
        self.assertEqual(possible_values, values_in_table)
        # checking some values in the table
        expected_dict = {(0x0, 0x0) : 16,
                         (0x7, 0x4) : 2,
                         (0x2, 0xb) : 0,
                         (0xA, 0xE) : 4}

        for coordinate in expected_dict.keys():
            self.assertEqual(expected_dict[coordinate], table[coordinate])
