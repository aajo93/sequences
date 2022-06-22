#!/usr/bin/env python3
import unittest
from main import cubed,squared,fibonacci,pascal

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_fibonacci(self):

        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(14), 377)
        self.assertEqual(fibonacci(69), 117669030460994)
        self.assertEqual(fibonacci(103), 1500520536206896083277)


    def test_pascal(self):
        self.assertEqual(pascal(0), [])
        self.assertEqual(pascal(1), [[1]])
        self.assertEqual(pascal(2), [[1],[1,1]])
        self.assertEqual(pascal(3), [[1],[1,1],[1,2,1]])
        self.assertEqual(pascal(4), [[1],[1,1],[1,2,1],[1,3,3,1]])
        self.assertEqual(pascal(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

    def test_squared(self):
        self.assertEqual(squared(0),[])
        self.assertEqual(squared(1),[1])
        self.assertEqual(squared(2),[1,4])
        self.assertEqual(squared(3),[1,4,9])
        self.assertEqual(squared(4),[1,4,9,16])
        self.assertEqual(squared(5),[1,4,9,16,25])
        self.assertEqual(squared(10),[1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
        self.assertEqual(squared(13),[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169])

    def test_cubed(self):
        self.assertEqual(cubed(0),[])
        self.assertEqual(cubed(1),[1])
        self.assertEqual(cubed(2),[1,8])
        self.assertEqual(cubed(3),[1,8,27])
        self.assertEqual(cubed(4),[1,8,27,64])
        self.assertEqual(cubed(5),[1,8,27,64,125])
        self.assertEqual(cubed(6),[1,8,27,64,125,216])
        self.assertEqual(cubed(7),[1,8,27,64,125,216,343])
        self.assertEqual(cubed(8),[1,8,27,64,125,216,343,512])


if __name__ == '__main__':
    unittest.main()
