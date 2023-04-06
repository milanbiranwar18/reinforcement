#Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#

def word_pattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """

    words = s.split()
    if len(pattern) != len(words):
        return False

    pattern_map = {}
    word_map = {}

    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]

        if letter not in pattern_map and word not in word_map:
            pattern_map[letter] = word
            word_map[word] = letter
        elif letter in pattern_map and word_map.get(word) != letter:
            return False
        elif word in word_map and pattern_map.get(letter) != word:
            return False

    return True


if __name__ == '__main__':
    print(word_pattern("abba", "dog cat cat dog"))
    print(word_pattern("abba", "dog cat cat fish"))
    print(word_pattern("aaaa", "dog cat cat dog"))