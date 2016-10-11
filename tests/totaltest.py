#! /usr/bin/env python3

# Full test for wordcounter

import wordcounter


def writetofile():
    wordcount_obj = wordcounter.WordCount("mobydick.txt")
    pretty_dict = wordcount_obj.get_result()
    with open("log.txt", "w+") as file1:
        file1.write(pretty_dict)

writetofile()
