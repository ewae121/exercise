# Deduplicator

Write a function with two arguments: a string and an integer.
The function will return a string that is similar to the first argument, but with certain duplicated characters removed.
The method should remove consecutive sequences of same character to ensure that the length of the sequence is no greater than the second integer argument.

Examples (maybe for unit testing):* "aaab", 2 => "aab"* "aabb", 1 => "ab"* "aabbaa", 1 => "aba"

Edge cases to also test:* "abcdefg", 1 => "abcdefg"* "abcdefg", 0 => ""* "", 100 => ""

To install

```
sudo apt install virtualenv
virtualenv --python=python3
source venv/bin/activate
make install
```

Usage, in a valid venv

```
python3 app.py --(venv) ewae@pluton:~/dev/excercise$ python3 app.py --help
usage: app.py [-h] input max_occurences

positional arguments:
  input           String to deduplicate
  max_occurences  Maximum of duplicated occurences

optional arguments:
  -h, --help      show this help message and exit
```

Example:
```
(venv) ewae@pluton:~/dev/excercise$ python3 app.py "jhdddddklkkkkjkljklj"  3
jhdddklkkkjkljklj
```

