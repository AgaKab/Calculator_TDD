import unittest
from calculator import Calculator
   
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(10,20), 30)
        self.assertEqual(-177, self.calculator.add(-123,-54))
        self.assertEqual(-10, self.calculator.add(10,-20))
        self.assertEqual(-10, self.calculator.add(-10,0))
        
    def test_subtract(self):
        self.assertEqual(10, self.calculator.subtract(20,10))
        self.assertEqual(98, self.calculator.subtract(99,1))
        
    def test_multiply(self):
        self.assertEqual(10, self.calculator.multiply(2,5))
        self.assertEqual(-8, self.calculator.multiply(2,-4))
        self.assertEqual(0, self.calculator.multiply(0,99))
    
    def test_divide(self):
        self.assertEqual(5, self.calculator.divide(25,5))
        self.assertEqual(-8, self.calculator.divide(32,-4))
        self.assertEqual(0, self.calculator.divide(0,99))
    
    def test_divide_by_zero(self):
        # self.assertEqual(self.calculator.divide(99,0), "Do not divide by zero!")
        with self.assertRaises(ValueError):
            self.calculator.divide(99, 0)
    
if __name__ == '__main__':
    unittest.main()