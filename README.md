Word Counter
---------
_It counts words?! WHOOOOOAAAAAAA!_

This is a program that takes a plain text or an html file as input and writes
a JSON formatted string to the output file.

The JSON string is in the format:

```json
{
    "File Name": "sample.file",
    "File Path": "/path/to/sample.file",
    "File type": "file",
    "Total Words": 1337,
    "Word Counts": {
        "each": 100,
        "word": 200,
        "count": 300,
        }
}
```
Note To Users
-------------

Please note that this program might not work the way you think a word counter should
work. There are special cases which are probably not covered in this program.

For example: any word with an apostrophe s (like "Fred's") is counted as the base 
word (i.e. it is considered as "Fred") whereas different forms of the same word
(like "fly", "flying", "flew") count as different words.

There might be other programs that do this job better and cover more file types so 
try to find which might work best for you.

##### Regarding HTML:

Please note that if you give an HTML file, the program will first strip out any
embedded Javascript and CSS and remove all the tags before performing the word 
count. Your original HTML file will remain intact.

How To Use
----------

* Clone the repository and cd into the directory
```bash
$ git clone https://github.com/dragsubil/word-counter
$ cd word-counter
```
* Execute run.py
```bash
$ python3 run.py <input file> <output file>
```
* Open your output file


License
-------

Licensed under GNU GPL v3.0. See the LICENSE file for details.
