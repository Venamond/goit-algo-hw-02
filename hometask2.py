import os
from collections import deque

def is_palindrome(s: str) -> bool:
    '''
        Check if a given string is a palindrome.
        Args:
            s (str): The string to check.
        Returns:
            bool: True if the string is a palindrome, False otherwise.  
    '''
    # ignore spaces and case differences
    filtered = (ch for ch in s if not ch.isspace())
    # create a deque with the filtered characters
    d = deque(ch.casefold() for ch in filtered)
    # compare characters from both ends
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

os.system("clear")
# examples
tests = [
    "Козак з казок",
    "Never odd or even",
    "Топот",
    "abc cba",
    "not a palindrome",
    "Я несу гусеня",
    "mam",
    "test",
    "козак",
    "вулиця",
    "око",
    "a",
    "in",
    "noon",
    "aa"
]

for t in tests:
    if is_palindrome(t):
        print(f"{t!r} -> \033[92mпаліндром\033[0m")
    else:
        print(f"{t!r} -> \033[91mне паліндром\033[0m")