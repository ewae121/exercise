# Deduplicator

[![Python application](https://github.com/ewae121/exercise/actions/workflows/python-app.yml/badge.svg)](https://github.com/ewae121/exercise/actions/workflows/python-app.yml)

**You can regard for time I spent using __git log__ command or regarding at the end**

Write a function with two arguments: a string and an integer.
The function will return a string that is similar to the first argument, but with certain duplicated characters removed.
The method should remove consecutive sequences of same character to ensure that the length of the sequence is no greater than the second integer argument.

Examples (maybe for unit testing):* "aaab", 2 => "aab"* "aabb", 1 => "ab"* "aabbaa", 1 => "aba"

Edge cases to also test:* "abcdefg", 1 => "abcdefg"* "abcdefg", 0 => ""* "", 100 => ""

![Last status](doc/images/readme/tests.png?raw=true "Available operations result")


## Install

To install and initiate venv:

```
sudo apt install virtualenv
virtualenv --python=python3
```

To get a valid venv:

```
source venv/bin/activate
make install
```

## Usage

In a valid venv:

```
python3 src/app.py --(venv) ewae@pluton:~/dev/excercise$ python3 app.py --help
usage: src/app.py [-h] input max_occurences

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

![Example](doc/images/readme/screenshot.png?raw=true "Launch example")


## Launch test

In a valid venv:

```
make test
```

## Launch formatter

In a valid venv:

```
make format
```

## Launch linters

In a valid venv:

```
make lint
make pylint
```

## Thanks

![Example](doc/images/readme/gitlog.png?raw=true "Gitlog")

Thank you for your time it was nice to talk you.
