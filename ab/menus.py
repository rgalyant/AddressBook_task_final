"""
Menus for AddressBook CLI
"""

from .Record import Record
from . import utils

def main():
    """
    Main menu for CLI.
    """

    print("1. Sort records")
    print("2. Search records")
    print("3. Add record")
    print("4. Edit record")
    print("5. Remove records")
    print("6. Exit")
    print("")

    try:
        selection = input("> ")
    except KeyboardInterrupt or EOFError:
        return 6
    
    print("")

    if not selection.isnumeric():
        print("Error: invalid input.\n")
        return None
    
    selection = int(selection)
    if 0 < selection <= 6:
        return selection
    else:
        print("Error: invalid menu option.\n")
        return None

def record(record=None, search=False):
    """
    Record data input menu for CLI.
    """
    
    if search:
        print("Enter search critera: case insensetive, ? - one any character")
        print("* - any number of any characters (including none).")
        print("Leave all field blank to select everything.")
        print("Press Ctrl + C to cancel.")
    else:
        print("Enter new values.")
        print("Press Ctrl + C to cancel. Any changes won't be saved.")

    print("")

    try:
        first_name = utils.rich_input("First name", record.first_name if record else None, search)
        last_name = utils.rich_input("Last name", record.last_name if record else None, search)
        phone = utils.rich_input("Phone", record.phone if record else None, search)
        address = utils.rich_input("Address", record.address if record else None, True)
        date_of_birth = utils.rich_input("Date of birth", record.date_of_birth if record else None, True)
    except KeyboardInterrupt or EOFError: # Ctrl+C will throw EOF when input is empty
        print("\nOperation calceled.\n")
        return None
    
    if record:
        record.first_name = first_name
        record.last_name = last_name
        record.phone = phone
        record.address = address
        record.date_of_birth = date_of_birth
    else:
        record = Record(first_name, last_name, phone, address, date_of_birth)
    
    print("")
    return record

def index(address_book, search=None, remove=False):
    """
    Indexing (listing) menu for CLI.
    """
    
    lengths = [10, 20, 20, 15, 15]
    template = " ".join(map(lambda l: f"{{:{l}}}", lengths))

    print(template.format("First name", "Last name", "Phone", "Address", "Date of birth"))
    print(template.format(*["=" * l for l in lengths]))

    to_remove = []
    for i, record in enumerate(address_book):
        if not search or \
            utils.match(record.first_name, search.first_name) and \
            utils.match(record.last_name, search.last_name) and \
            utils.match(record.phone, search.phone) and \
            utils.match(record.address or "", search.address) and \
            utils.match(record.date_of_birth or "", search.date_of_birth):

            print(template.format(record.first_name, record.last_name, record.phone,
                record.address or "", record.date_of_birth or ""))
            
            if remove:
                to_remove.append(i)
    
    if remove:
        consent = yes_no("Do you realy want to remove these records?", False)
        if consent:
            to_remove.reverse()
            for i in to_remove:
                del address_book[i]
        else:
            print("Operation calceled.")
    
    print("")

def yes_no(prompt, default=True):
    """
    Yes/no dialog for CLI.
    """
    
    print(prompt)
    print("")
    while True:
        try:
            value = input(("Y/n" if default else "y/N") + " > ").lower()
        except KeyboardInterrupt or EOFError:
            return False

        if not value:
            value = default
        elif value == "y":
            value = True
        elif value == "n":
            value = False
        else:
            print("Error: incorrect input.")
            continue
        return value