import unittest
from password_check import is_valid_password

class TestPassword(unittest.TestCase):
    def testincorrect_password(self):
        self.assertEqual(is_valid_password("abc123"),False)
    def testcorrect_password(self):
        self.assertEqual(is_valid_password("Abcdef12"),True)
    def testnotenoughletter(self):
        self.assertEqual(is_valid_password("Mina34"),False)
    def testlettersonly(self):
        self.assertEqual(is_valid_password("obsonlas"),False)
    
        
if __name__ == "__main__":
    unittest.main()