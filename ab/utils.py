"""
Util methods for CLI.
"""

def sort(array, less_comparator):
    """
    Sort array using selection sort.
    """

    for i in range(len(array)):
        min_i = i
        for j in range(i, len(array)):
            if less_comparator(array[j], array[min_i]):
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
        
def rich_input(field, current=None, optional=False):
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

    # It is case-insensetive
    string = string.lower()
    pattern = pattern.lower()

    # I'm pretty sure you can optimize this
    star_parts = pattern.split("*")
    star_part_last_idex = len(star_parts) - 1
    for i, star_part in enumerate(star_parts):
        if "?" in star_part:
            for question_part in star_part.split("?"):
                if match > len(string): break
                starts = string.startswith(question_part, match)
                if not starts: break
                match += len(question_part) + 1
            else:
                match -= 1
                continue
            match = -1
            break
        else:
            match = string.find(star_part, match) if 0 < i < star_part_last_idex else \
                string.startswith(star_part) - 1 if i == 0 else string.endswith(star_part) - 1
            if match == -1: break
            match += len(star_part)
    return match != -1