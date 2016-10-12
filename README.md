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
	...
    }
}
```

(Please note that this thing is not quite as usable as you might like. There are
loads of special cases which are probably not covered in this program. And some
things might not work the way you want it to.

For example: any word with an apostrophe s (like "Fred's") is counted as the base 
word (i.e. it is considered as "Fred") whereas different forms of the same word
(like "fly", "flying", "flew") count as different words.

There are other programs that do this job better and cover more file types so you're
better off using those.)

How To Use
----------

1. Clone the repository and cd into the directory
```bash
$ git clone https://github.com/dragsubil/word-counter
$ cd word-counter
```
2. Execute run.py
```bash
$ python3 run.py <input file> <output file>

3. Open your output file


License
-------

See LICENSE
