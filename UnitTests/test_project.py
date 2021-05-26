"""
Write a class and 2 methods named: count_characters() which accepts a character string 
and which returns the occurrence of the characters contained in the string in the form of a dictionary.
count_words() which accepts a character string and which returns the occurrence of the words contained 
in the string as a dictionary. Create test with patch (return_value) for the both methods consequently 
in 2 different tests.
"""

from unittest import TestCase, mock, main
from unittest.case import skip
from Project import Count


class TestCount (TestCase):
    count_char_dict = {'c' : 2, 'o' : 1, 'd' : 2, 'e' : 2, 'a' : 2, 'm' : 1, 'y' : 1}
    count_words_dict = {'hello' : 2, 'world' : 2, 'how' : 1, 'are' : 1, 'you' : 1, 'today' : 1}
    def setUp(self) -> None:
        self.test_class = Count()
        self.test_count_char = "CodeAcademy"
        self.test_count_words = "Hello, hello world. How are you today, world!"
        #self.count_char_dict = {'c' : 2, 'o' : 1, 'd' : 2, 'e' : 2, 'a' : 2, 'm' : 1, 'y' : 1}
        
    #@mock.patch('Project.Count.count_characters', return_value = count_char_dict)
    # def test_count_characters(self, count_characters): 
    #     self.assertEqual(count_characters(self.test_count_char), self.count_char_dict)
    def test_count_characters(self): 
        self.assertEqual(self.test_class.count_characters(self.test_count_char), self.count_char_dict)

    # @mock.patch('Project.Count.count_words', return_value = count_words_dict)
    # def test_count_words(self, count_words):
    #     self.assertEqual(count_words(self.test_count_words), self.count_words
    def test_count_words(self):
        self.assertEqual(self.test_class.count_words(self.test_count_words), self.count_words_dict)


if __name__ == "__main__":
    main()
