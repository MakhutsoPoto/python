import unittest
from rectangle_area import*

class TestCase(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(rectangle_area(2,3),"This is the area: 6")
    def test_wrong_numbers(self):
        self.assertNotEqual(rectangle_area(2,3),'6')
    def test_big_numbers(self):
        self.assertEqual(rectangle_area(100,50),'This is the area: 5000')
    def test_int_numbers(self):
        self.assertEqual(rectangle_area(5,12),"This is the area: 60")

if __name__ == "__main__":
    unittest.main()