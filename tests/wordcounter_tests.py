#!/usr/bin/env python3

# Tests for the classes in wordcounter.py

import unittest
import wordcounter


class wordcounterTests(unittest.TestCase):

    def setUp(self):
        self.wordcount_txt = wordcounter.WordCount("loren.txt")
        self.wordcount_html = wordcounter.WordCount("loren.html")
        self.filetype = type(open("loren.txt"))

    def test_identify_filetype(self):
        self.assertEqual(self.wordcount_txt.identify_filetype(), 'txt')
        self.assertEqual(self.wordcount_html.identify_filetype(), 'html')

    def test_get_file(self):
        self.assertIsInstance(self.wordcount_txt.get_file(), self.filetype)
        self.assertIsInstance(self.wordcount_html.get_file(), self.filetype)

    def test_call_processtext(self):
        self.assertIsInstance(self.wordcount_txt.call_processtext(), dict)

if __name__ == '__main__':
    unittest.main()
