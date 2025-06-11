import unittest
from fib_sum import sum_even_fibonacci

class TestFib(unittest.TestCase):
    def testsmall(self):
        self.assertEqual(sum_even_fibonacci(10),10)
    def testbig(self):
        self.assertEqual(sum_even_fibonacci(34),44)
        
if __name__ == "__main__":
    unittest.main()