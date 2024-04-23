import unittest
from calculator import Calculator

    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def add_test(self):
        self.assertEqual(30, self.calculator.add(10,20))
        self.assertEqual(-177, self.calculator.add(-123,-54))
        self.assertEqual(-10, self.calculator.add(10,-20))
        self.assertEqual(-10, self.calculator.add(-10,0))


if __name__ == '__main__':
    unittest.main()