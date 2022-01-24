"""
Util methods for CLI.
"""

def sort(array, less_comparator):
    """
    Sort array using selection sort.
    """

    for i in range(len(array)):
        mini = i
        for j in range(i, len(array)):
            if less_comparator(array[j], array[mini]):
                mini = j
        array[i], array[mini] = array[mini], array[i]
        
def rich_input(field, current= None, optional = False):
    """
    Feature-rich input for record values.
    """

    prompt = "{}{}{}{}: ".format("(Optional) " if optional else "",
        field, ", '-' to reset" if optional and current else "",
        " or leave it blank to keep " + current if current else "")
    while True:
        value = input(prompt)
        if value or current or optional:
            if not value and current:
                value = current
            elif value == '-' and optional:
                value = None
            return value
        print("Error: incorrect input.")

def match(string, pattern):
    """
    Check string for match to glob-like pattern.
    """
    
    match = 0

    string = string.lower()
    pattern = pattern.lower()

    # I'm pretty sure you can optimize this
    star_parts = pattern.split("*")
    spLast = len(star_parts) - 1
    for i, part in enumerate(star_parts):
        if "?" in part:
            for qpart in part.split("?"):
                if match > len(string): break
                starts = string.startswith(qpart, match)
                if not starts: break
                match += len(qpart) + 1
            else:
                match -= 1
                continue
            match = -1
            break
        else:
            match = string.find(part, match) if 0 < i < spLast else \
                string.startswith(part) - 1 if i == 0 else string.endswith(part)
            if match == -1: break
            match += len(part)
    return match != -1