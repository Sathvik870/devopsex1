import unittest

from calculator import evaluate


class TestCalculator(unittest.TestCase):
    def test_basic_add(self):
        self.assertEqual(evaluate("2+3"), 5)

    def test_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14)

    def test_division(self):
        self.assertAlmostEqual(evaluate("7/2"), 3.5)

    def test_power_with_hat(self):
        self.assertEqual(evaluate("2^3"), 8)

    def test_power_with_double_star(self):
        self.assertEqual(evaluate("3**2"), 9)

    def test_unary(self):
        self.assertEqual(evaluate("-5+2"), -3)

    def test_mod(self):
        self.assertEqual(evaluate("10 % 3"), 1)

    def test_invalid_syntax(self):
        with self.assertRaises(ValueError):
            evaluate("2 + (3")

    def test_names_forbidden(self):
        with self.assertRaises(ValueError):
            evaluate("os.system('echo hi')")


if __name__ == "__main__":
    unittest.main()
