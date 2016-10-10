#!/usr/bin/env python3

# Fairly simple python program (or is it a library? I don't these things)
# to obtain a JSON of the count of all the words in a file.

import processtext


class WordCount():
    '''This class is our interface (not in the Java sense) to theprocesstext.py classes.
    If someone has better terms for what this class is, please tell me.'''

    def __init__(self, filepath=None):
        self.filepath = filepath
        self.filetype = None
        self.fileobject = None
        self.word_dictionary = None

    def identify_filetype(self):
        fpath = self.filepath
        fpath = fpath.split('.')
        return fpath[-1]

    def get_file(self):
        fobj = open(self.filepath, 'r+', encoding="UTF-8")
        return fobj

    def call_processtext(self):
        if(self.filetype == 'html')
            return processtext.ProcessHTML(self.fileobject)
        else:
            return processtext.ProcessPlainTxt(self.fileobject)

    def get_JSON(self):
        pass

    def get_result(self, filepath):
        self.filepath = filepath
        self.filetype = self.identify_filetype()
        self.fileobject = self.get_file()
