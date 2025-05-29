import unittest
"""
unit tests
"""

class Calculator:
    """
    Calculator class
    """
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor
    
    def add(self, value1: float, value2: float) -> float: 
        return value1 + value2
    

class TestCalculatorClass(unittest.TestCase):
    def test_positive_dividend(self):
        self.assertEqual(Calculator.divide(self, 10, 5), 2)

    def test_negative_dividend(self):
        self.assertEqual(Calculator.divide(self, -10, 5), -2)

    def test_positive_divisor(self):
        self.assertEqual(Calculator.divide(self, 10, 2), 5)

    def test_negative_divisor(self):
        self.assertEqual(Calculator.divide(self, 10, -2), -5)

    def test_large_dividend(self):
        self.assertEqual(Calculator.divide(self, 1000, 2), 500)

    def test_large_divisor(self):
        self.assertEqual(Calculator.divide(self, 10, 2000), 0.005)

    def test_str_dividend(self):
        with self.assertRaises(TypeError):
            Calculator.divide(self, "Hello", 2)
    
    def test_str_divisor(self):
        with self.assertRaises(TypeError):
            Calculator.divide(self, 10, "World")

    def test_divide_str(self):
        with self.assertRaises(TypeError):
            Calculator.divide(self, "Hello", "World")


if __name__ == '__main__':
    unittest.main()
