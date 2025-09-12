import unittest
max_integer = __import__('6-max_integer').max_integer

class testmaxinteger(unittest.TestCase):
    def test_list(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([3]), 3)
        self.assertAlmostEqual(max_integer(["a", "b", "c"]), "c")
    def test_errors(self):
        self.assertRaises(TypeError, max_integer, None)
    