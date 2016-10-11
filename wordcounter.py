#!/usr/bin/env python3

# Fairly simple python program (or is it a library? I don't these things)
# to obtain a JSON of the count of all the words in a file.

import os
import processtext
import pprint


class WordCount():
    '''This class is our interface (not in the Java sense) to theprocesstext.py classes.
    If someone has better terms for what this class is, please tell me.
    '''

    def __init__(self, filepath=None):
        self.filepath = filepath
        self.filetype = None
        self.fileobject = None
        self.word_dictionary = None

    def validate_filepath(self, filepath):
        if self.filepath is None or not os.path.exists(self.filepath):
            if self.filepath is None and filepath is None:
                self.filepath = str(input("Enter file path: "))
            else:
                self.filepath = filepath

            self.validate_filepath(filepath)

    def identify_filetype(self):
        fpath = self.filepath
        fpath = fpath.split('.')
        return fpath[-1]

    def get_file(self):
        fobj = open(self.filepath, 'r+', encoding="UTF-8")
        return fobj

    def call_processtext(self):
        if(self.filetype == 'html'):
            p_obj = processtext.ProcessHTML(self.fileobject)
            return p_obj.get_dict()
        else:
            p_obj = processtext.ProcessPlainTxt(self.fileobject)
            return p_obj.get_dict()

    def get_JSON(self):
        pass

    def get_result(self, filepath=None):
        self.validate_filepath(filepath)
        self.filetype = self.identify_filetype()
        self.fileobject = self.get_file()
        self.word_dictionary = self.call_processtext()
        return pprint.pformat(self.word_dictionary)

