import string
import re
"""
Write a class and 2 methods named: count_characters() which accepts a character string 
and which returns the occurrence of the characters contained in the string in the form of a dictionary.
count_words() which accepts a character string and which returns the occurrence of the words contained 
in the string as a dictionary. Create test with patch (return_value) for the both methods consequently 
in 2 different tests.

"""

class Count:
    def __init__(self):
        pass
    
    def count_characters(self, text):
        text = text.lower()
        dictionary = {}

        for c in text:
            if c in dictionary.keys():
                dictionary[c] += 1
            else:
                dictionary[c] = 1
            
        return dictionary

    def count_words(self, text):
        dictionary = {}
        #text = re.sub(r'[^\w\s]', '',text)
        
        for c in text:
            if c in string.punctuation:
                text = text.replace(c, '')

        words = text.lower().split(' ')

        for word in words:
            if word not in dictionary.keys():
                dictionary[word] = 1
            else:
                dictionary[word] += 1
            
        return dictionary

count = Count()
print(count.count_characters("CodeAcademy"))
print(count.count_words("Hello, hello world. How are you today, world!"))
