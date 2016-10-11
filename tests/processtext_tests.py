#!/usr/bin/env python3

# This contains the tests for the classes in processtext.py


import unittest
import processtext
from pprint import pprint

class processtextTests(unittest.TestCase):

    def setUp(self):
        self.test_file = open("loren.txt", "r+", encoding="UTF-8")
        self.processtext_obj = processtext.ProcessText(self.test_file)
        self.processtext_obj.file_object.seek(0)

    def test_get_dict(self):
        self.assertIsInstance(self.processtext_obj.get_dict(), dict)

    def test_strip_parse_line(self):
        wordlist, _ = self.processtext_obj.strip_parse_line()
        self.assertIsInstance(wordlist, list)
        print(wordlist)

    def test_add_to_dict(self):
        wordlist, word_dict = self.processtext_obj.strip_parse_line()
        self.assertIsInstance(word_dict, dict)
        pprint(word_dict)

    def tearDown(self):
        self.test_file.close()

if __name__ == '__main__':
    unittest.main()
