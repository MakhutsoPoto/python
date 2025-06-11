import unittest 
from name_change import reformat_name

class TestCase(unittest.TestCase):
    def testJohn(self):
        self.assertEqual(reformat_name(" john DOE "),"Doe, John")
    def testAlice(self):
        self.assertEqual(reformat_name("ALICE smith"),"Smith, Alice")
        
if __name__ == "__main__":
    unittest.main()