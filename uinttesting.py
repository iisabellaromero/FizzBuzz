import unittest
from fizzbuzz import fizzbuzz 

class TestFizzBuzz(unittest.TestCase):
    
    # Happy path tests
    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        
    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        
    def test_number(self):
        self.assertEqual(fizzbuzz(2), "2")
        
    # Edge cases
    def test_negative_fizz(self):
        self.assertEqual(fizzbuzz(-3), "Fizz")
        
    def test_negative_buzz(self):
        self.assertEqual(fizzbuzz(-5), "Buzz")
        
    def test_negative_fizzbuzz(self):
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        
    def test_zero(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")
        
    def test_large_number(self):
        self.assertEqual(fizzbuzz(300), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()
