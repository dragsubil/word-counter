#! /usr/bin/env python3

# Full test for wordcounter

import wordcounter



def writetofile(filename, op_file):
    wordcount_obj = wordcounter.WordCount(filename)
    pretty_dict = wordcount_obj.get_result()
    with open(op_file, "w+") as file1:
        file1.write(pretty_dict)


writetofile("aliceinwonderland.txt", "alice.json")
writetofile("worm.html", "worm.json")
