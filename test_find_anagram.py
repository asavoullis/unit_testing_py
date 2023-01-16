import unittest
from find_anagram import find_anagrams

class TestFindAnagrams(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Class-level setup - runs before anything """
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        """ Class-level teardown - runs after everything """
        print('teardownClass')

    def setUp(self):
        """ Method-level setup - runs before every single test """
        print('setUp')

    def tearDown(self):
        """ Method-level teardown - runs after every single test """
        print('tearDown\n')

    def test_find_anagrams_same_word(self):
        # Test if the function correctly identifies anagrams for the same word
        word = "listen"
        result = find_anagrams(word)
        expected = {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
        self.assertEqual(result, expected)

    def test_find_anagrams_different_words(self):
        # Test if the function correctly identifies non-anagrams
        word1 = "listen"
        word2 = "silents"
        result1 = find_anagrams(word1) 
        result2 = find_anagrams(word2)
        self.assertNotEqual(result1, result2)

    def test_find_anagrams_anagrams(self):
        # Test if the function correctly identifies anagrams
        word1 = "listen"
        word2 = "silent"
        result1 = find_anagrams(word1)
        result2 = find_anagrams(word2)
        self.assertEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()
