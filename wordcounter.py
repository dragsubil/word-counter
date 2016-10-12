#!/usr/bin/env python3

# This file contains the WordCount class which takes a filepath (either
# through initializing class object processtext.ProcessText(filepath) or 
# through the method ProcessText.get_result(filepath) ).
# The get_result() method will return a JSON formatted string containing
# the filename, filepath, total word count and individual word counts.

import os
import processtext
import json


class WordCount():
    '''This class is our interface (not in the Java sense) to theprocesstext.py classes.
    If someone has better terms for what this class is, please tell me.
    '''

    def __init__(self, filepath=None):
        self.filepath = filepath
        self.filetype = None
        self.fileobject = None
        self.word_dictionary = None
        self.p_object = None

    def validate_filepath(self, filepath=None):
        if filepath is not None and os.path.exists(filepath):
            self.filepath = filepath
            return
        if self.filepath is None or not os.path.exists(self.filepath):
            self.filepath = str(input("Enter proper file path: "))
            self.validate_filepath()
        else:
            return

    def identify_filetype(self):
        fpath = self.filepath
        fpath = fpath.split('.')
        return fpath[-1]

    def get_file(self):
        fobj = open(self.filepath, 'r+', encoding="UTF-8")
        return fobj

    def call_processtext(self):
        '''Initializes the filetype specific class object and returns a dictionary
        containing total total and individual word counts.
        '''

        if(self.filetype == 'html'):
            self.p_object = processtext.ProcessHTML(self.fileobject)
            return self.p_object.get_dict()
        else:
            self.p_object = processtext.ProcessPlainTxt(self.fileobject)
            return self.p_object.get_dict()

    def get_JSON(self):
        '''returns a JSON formatted string with filename, filetype, path, and
        total and individual word counts
        '''
    
        json_dict = {
            "File Name": os.path.basename(self.filepath),
            "File Path": os.path.abspath(self.filepath),
            "File type": self.filetype,
            "Total Words": self.word_dictionary["total_count"],
            "Word Counts": self.word_dictionary["individual_count"]
             }
        return json.dumps(json_dict, sort_keys=True, indent=4)

    def get_result(self, filepath=None):
        '''The primary method that does the work of calling the required
        methods of the class in the correct order to get the final required
        JSON string.
        If a filepath is passed with this method, it overwrites the content of
        self.filepath.
        '''

        self.validate_filepath(filepath)
        self.filetype = self.identify_filetype()
        self.fileobject = self.get_file()
        self.word_dictionary = self.call_processtext()
        return self.get_JSON()
