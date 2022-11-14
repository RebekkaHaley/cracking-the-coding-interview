"""
Functions for section '1. Arrays and Strings' of 'Chapter IX: Interview Questions'.
"""


def is_unique(string: str) -> bool:
    """Checks whether all chars in a given string appear only once.

    Args:
        string: Any string.

    Returns:
        True if all characters are unique. Else False.
    """
    memory = ''
    for char in string:
        if char in memory:
            return False
        memory = f'{memory}{char}'
    return True


def check_permutation(string: str, target: str) -> bool:
    """Checks whether one string is a permutation of the other.

    Args:
        string: Any string.
        target: Potential permutation of 'string'.

    Returns:
        True if 'target' is a permutation of 'string'. Else False.
    """
    if sorted(string) == sorted(target):
        return True
    return False


def urlify(string: str, true_len: int) -> str:
    """Converts string to a URL by replacing whitespace with '%20'.

    Args:
        string: Any string.
        true_len: Length of non-URL string with no trailing whitespace.

    Returns:
        URL string.
    """
    url = [char for char in string.strip()]
    for i in range(true_len):
        if url[i] == ' ':
            url[i] = '%20'
        else:
            continue
    return ''.join(url)


def one_away(before: str, after: str) -> bool:
    """Checks whether an edit to the 'before' string is one away from the 'after'.

    There are three types of edits: insert a char, remove a char, or replace a char.

    Args:
        before: String before an edit.
        after: Edited string.

    Returns:
        True if a one-away edit. Else false.
    """
    if len(before) == len(after):  # checks replacements
        difference = len(set(before) - set(after))
    elif len(before) > len(after):  # checks removals
        difference = len(set(before) - set(after))
    else:  # checks inserts
        difference = len(set(after) - set(before))
    if difference < 2:
        return True
    return False
