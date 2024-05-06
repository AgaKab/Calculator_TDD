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

if __name__ == '__main__':
    unittest.main()