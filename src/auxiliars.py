import operator as op

def bidirectional_subset(ls1: list, ls2: list) -> bool:
    for i in ls1:
        if op.countOf(ls1, i) != op.countOf(ls2, i):
            return False
    if(len(ls1) != len(ls2)):
        return False
    return True

def clean_string(s: str) -> str:
    # Remove leading and trailing spaces
    s = s.strip()
    # Replace one or more spaces with a single underscore
    s = '_'.join(s.split())
    return s

def get_matching_index(lst, element):
    """
    Returns the index of the first occurrence of the external element in the list.

    Args:
        lst (list): The list to search through.
        element: The element to match.

    Returns:
        int: The index of the matching element, or -1 if no match is found.
    """
    for index, item in enumerate(lst):
        if item == element:
            return index
    return False
