import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(0, 0), 0)
        with self.assertRaises(TypeError):
            self.calc.add('a', 3)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        with self.assertRaises(TypeError):
            self.calc.subtract('a', 3)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        with self.assertRaises(TypeError):
            self.calc.multiply('a', 3)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(0, 5), 0)
        with self.assertRaises(TypeError):
            self.calc.divide('a', 3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
