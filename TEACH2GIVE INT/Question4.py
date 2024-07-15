#Design a function that determines whether a given string is a pangram. A
#pangram is a sentence or phrase containing every letter of the alphabet at
#least once. Punctuation and case are typically ignored. For example, the
#string "The quick brown fox jumps over the lazy dog" is a pangram, while
#"Hello, world!" is not.

def is_pangram(s):
    """
    Returns True if the input string is a pangram, False otherwise.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()  # ignore case
    s = ''.join(e for e in s if e.isalnum())  # remove punctuation and whitespace
    return set(alphabet).issubset(set(s))  # check if all alphabet letters are present