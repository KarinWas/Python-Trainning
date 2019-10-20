import unittest
from primes import check_a_smaller_b, check_prime

class TestFactorial(unittest.TestCase):
    def test_equal_nums(self):
        self.assertFalse(check_a_smaller_b(10, 10))
    
    def test_a_bigger_b(self):
        self.assertFalse(check_a_smaller_b(10, 4))
    
    def test_a_smaller_b(self):
        self.assertTrue(check_a_smaller_b(2, 10))
    
    def test_composite_number(self):
        self.assertFalse(check_prime(6))
    
    def test_prime_number(self):
        self.assertTrue(check_prime(11))

if __name__ == '__main__':
    unittest.main()