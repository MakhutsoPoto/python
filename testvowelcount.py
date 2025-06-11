import unittest
from vowelcount import count_vowels


class TestVowels(unittest.TestCase):
    def testnovowels(self):
        self.assertEqual(count_vowels("bcd"),0)
    def testnoletters(self):
        self.assertEqual(count_vowels(""),0)
    def testallvowels(self):
        self.assertEqual(count_vowels("aeiou"),5)
    def testallvowelscap(self):
        self.assertEqual(count_vowels('AEIOU'),5)
    def testmixedvowels(self):
        self.assertEqual(count_vowels('AEiou'),5)
    def testonlyonevowel(self):
        self.assertEqual(count_vowels("CAR"),1)
    def testlongstring(self):
        self.assertEqual(count_vowels("Pulchritudinous"),6)
        self.assertEqual(count_vowels("Anemoiapolis"),7)
        
if __name__ == "__main__":
    unittest.main()
    