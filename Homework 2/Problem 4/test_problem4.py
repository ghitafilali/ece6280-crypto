import unittest
import problem4


class TestProblem4(unittest.TestCase):
    def test_rot_word(self):
        word = [0x61, 0x93, 0xc6, 0xea]
        self.assertEqual([0x93, 0xc6, 0xea, 0x61], problem4.rot_word(word))

    def test_sub_word(self):
        word = [0x61, 0x93, 0xc6, 0xea]
        self.assertEqual([0xef, 0xdc, 0xb4, 0x87], problem4.sub_word(word))
