import unittest

from translator import english_to_french, french_to_english
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when the input is Hello
        message = "Test value is not none."
        self.assertIsNotNone(english_to_french(None), message)  #test when the input is null
        


class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when the input is Bonjour
        message = "Test value is not none."
        self.assertIsNotNone(french_to_english(None), message) # test when the input is null
        
unittest.main()