Write a function with two arguments: a string and an integer.
The function will return a string that is similar to the first argument, but with certain duplicated characters removed.
The method should remove consecutive sequences of same character to ensure that the length of the sequence is no greater than the second integer argument.

Examples (maybe for unit testing):* "aaab", 2 => "aab"* "aabb", 1 => "ab"* "aabbaa", 1 => "aba"

Edge cases to also test:* "abcdefg", 1 => "abcdefg"* "abcdefg", 0 => ""* "", 100 => ""

