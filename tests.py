import unittest
from translator import frenchToEnglish
from translator import englishToFrench


class TestEnglishToFrench(unittest.TestCase): 
    def test_english_To_French(self): 
        self.assertEqual(englishToFrench("hello"),"bonjour")
        self.assertEqual(englishToFrench("love"),"l'amour")


class TestFrenchToEnglish(unittest.TestCase): 
    def test_french_To_English(self):
        self.assertEqual(frenchToEnglish('Je vous remercie'), 'Thank you')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
       
unittest.main()