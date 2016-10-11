#!/usr/bin/env python3

# This contains the class ProcessText and the subclasses that are created
# for each textfile type (currently only classes for txt and html).

import re

# Regex patterns needed for removing the punctuations
general_punctuations = re.compile(r'["@!&*,”“:?.;~`()]')
apostrophe_s = re.compile(r"'s\s")
double_dash = re.compile(r'--')
any_whitespace = re.compile(r'\s')
single_quotes = re.compile(r'^"|"$')
double_quotes = re.compile(r"^'|'$")


class ProcessText:

    def __init__(self, fileobj):
        self.file_object = fileobj
        self.word_dictionary = {}

    def strip_parse_line(self):
        '''This function will remove punctuations (see punctuation_string) unless
        its an apostrophe. After the punctuations are removed, the resultant list 
        of words is passed to the add_to_dict() function
        '''

        self.file_object.seek(0)
        for line in self.file_object:
            line = line.lower()
            line = general_punctuations.sub(' ', line)
            line = apostrophe_s.sub(' ', line)
            line = double_dash.sub(' ', line)
            wordlist = line.split(" ")
            wordlist = [any_whitespace.sub('', x) for x in wordlist]
            wordlist = [single_quotes.sub('', x) for x in wordlist]
            wordlist = [double_quotes.sub('', x) for x in wordlist]
            wordlist = [x for x in wordlist if x != '']
            self.add_to_dict(wordlist)

        del self.word_dictionary['-'] #  Removes '-' from the dict
        return (wordlist, self.word_dictionary)  # This line used only for tests 

    def add_to_dict(self, wordlist):
        '''This function will take the list of words passed to it and add it
        to the word_dictionary. The word_dictionary contains words as keys
        and number of its occurences as the value pair. If a word in the given list
        is already present in the word_dictionary, the corresponding value pair
        is incremented
        '''

        for i in wordlist:
            try:
                self.word_dictionary[i] += 1
            except KeyError:
                self.word_dictionary[i] = 1

    def get_dict(self):
        self.strip_parse_line()
        return self.word_dictionary


class ProcessPlainTxt(ProcessText):
    '''This class inherits from the ProcessText class and basically uses only
    the methods defined in that class
    '''

    def __init__(self, fileobj):
        super().__init__(fileobj)


class ProcessHTML(ProcessText):
    pass
