#!/usr/bin/env python3

# Tests for the classes in wordcounter.py

import unittest
import wordcounter


class wordcounterTests(unittest.TestCase):

    def setUp(self):
        self.wordcounter_txt = wordcounter.WordCount("loren.txt")
        self.wordcounter_html = wordcounter.WordCount("loren.html")
        self.filetype = type(open("loren.txt"))

    def test_identify_filetype(self):
        self.assertEqual(self.wordcounter_txt.identify_filetype(), 'txt')
        self.assertEqual(self.wordcounter_html.identify_filetype(), 'html')

    def test_get_file(self):
        self.assertIsInstance(self.wordcounter_txt.get_file(), self.filetype)
        self.assertIsInstance(self.wordcounter_html.get_file(), self.filetype)

    def test_call_processtext(self):
        self.wordcounter_txt.fileobject = self.wordcounter_txt.get_file()
        self.wordcounter_html.fileobject = self.wordcounter_html.get_file()
        self.assertIsInstance(self.wordcounter_txt.call_processtext(), dict)
        self.assertIsInstance(self.wordcounter_html.call_processtext(), dict)

    def test_get_result(self):
        pass

if __name__ == '__main__':
    unittest.main()
