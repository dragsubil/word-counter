#!/usr/bin/env python3

# This contains the class ProcessText and the subclasses that are created
# for each textfile type (currently only classes for txt and html).
# It performs the task of reading the file passed and producing a dictionary
# containing the total word count and the individual word count.
# This dictionary is returned to the caller.

import re
import os

# General regex patterns needed for removing the punctuations
general_punctuations = re.compile(r'["@|!&*,”“:?.;\-\[\]~`()]')  # All symbols between the [] 
                                                                # will be removed.
apostrophe_s = re.compile(r"'s\s")
apostrophe_s_u2019 = re.compile(r"’s\s")  # Special unicode character
single_dash = re.compile(r'-')
double_dash = re.compile(r'--')
any_whitespace = re.compile(r'\s')
single_quotes_u2018_u2019 = re.compile(r"‘|’")
single_quotes = re.compile(r"^'|'$")  # start and end quotes

# HTML specific regex patterns to remove tags and whatnot
style_pattern = re.compile("<style(.|\n)*?</style>")
script_pattern = re.compile("<script(.|\n)*?</script>")
html_comment_pattern = re.compile("<!--(.|\n)*?-->")
tag_pattern = re.compile("<(.|\n)*?>")
html_nbsp = re.compile("&nbsp")


class ProcessText:
    '''This is the base class inherited by the classes for each filetype.
    '''

    def __init__(self, fileobj):
        self.file_object = fileobj
        self.word_dictionary = {}
        self.word_count = 0

    def strip_parse_line(self):
        '''This function will remove punctuations and other symbols from each
        line of the file (held by self.file_object), converts the line to a
        list and then passes the list to the add_to_dict() function.
        The symbols to be removed are defined by the regex patterns at the
        top of the file.
        It returns a list of the words from the last line in the file and
        returns a dictionary with the word counts of each unique word in the
        file.
        '''

        self.file_object.seek(0)
        for line in self.file_object:
            line = line.lower()
            line = general_punctuations.sub(' ', line)
            line = apostrophe_s.sub(' ', line)
            line = apostrophe_s_u2019.sub(' ', line)
            wordlist = line.split(' ')
            wordlist = [any_whitespace.sub('', x) for x in wordlist]
            wordlist = [single_quotes_u2018_u2019.sub("'", x) for x in wordlist]
            wordlist = [single_quotes.sub('', x) for x in wordlist]
            wordlist = [x for x in wordlist if x != '']
            self.add_to_dict(wordlist)

        return (wordlist, self.word_dictionary)  # This line used only for tests

    def add_to_dict(self, wordlist):
        '''This function will take the list of words passed to it and add it
        to the word_dictionary. The word_dictionary contains words as keys
        and number of its occurences as the value pair. If a word in the given
        list is already present in the word_dictionary, the corresponding value
        is incremented.
        It also keeps track of the total word count (with self.word_count)
        '''

        for i in wordlist:
            try:
                self.word_dictionary[i] += 1
            except KeyError:
                self.word_dictionary[i] = 1
            self.word_count += 1

    def get_dict(self):
        '''Returns a dictionary containing the total word count and the count
        of the individual words.
        '''

        self.strip_parse_line()
        self.word_dictionary = {
            "total_count": self.word_count,
            "individual_count": self.word_dictionary
        }
        return self.word_dictionary

    def __del__(self):
        self.file_object.close()


class ProcessPlainTxt(ProcessText):
    '''This class inherits from the ProcessText class and basically uses only
    the methods defined in that class
    '''

    def __init__(self, fileobj):
        super().__init__(fileobj)


class ProcessHTML(ProcessText):
    '''This class does the word count of an HTML file. It first removes the
    contents between the <script></script> and the <style></style> tags and
    removes all the tags completely. This modified file is then passed to the
    get_dict() function in the parent class to do the rest.
    '''

    def __init__(self, fileobj):
        super().__init__(fileobj)
        self.backup_file = open("htmlbak", "w+")

    def remove_html_stuff(self):
        big_file_string = self.file_object.read()
        big_file_string = style_pattern.sub(" ", big_file_string)
        big_file_string = script_pattern.sub(" ", big_file_string)
        big_file_string = html_comment_pattern.sub(" ", big_file_string)
        big_file_string = tag_pattern.sub(" ", big_file_string)
        big_file_string = html_nbsp.sub(" ", big_file_string)
        self.backup_file.write(big_file_string)

    def get_dict(self):
        self.remove_html_stuff()
        self.file_object.close()
        self.file_object = self.backup_file
        return super().get_dict()

    def __del__(self):
        self.backup_file.close()
        os.remove("htmlbak")
