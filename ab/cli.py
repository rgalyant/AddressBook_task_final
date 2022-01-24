from . import utils
from . import menus

def cli(address_book):
    """
    Basic CLI implementation.
    """
    
    while True:
        selection = menus.main()

        if selection == 1:
            sort = menus.yes_no("Sort by first name?")
            if sort:
                utils.sort(address_book, lambda a, b: a.first_name < b.first_name)
            else:
                sort = menus.yes_no("Sort by last name?")
                if sort:
                    utils.sort(address_book, lambda a, b: a.last_name < b.last_name)
                else:
                    print("\nOperation calceled.\n")
        elif selection == 2:
            search = menus.record(search=True)
            if search:
                menus.index(address_book, search)
        elif selection == 3:
            record = menus.record()
            if record:
                address_book.append(record)
        elif selection == 4:
            address_book_length = len(address_book)
            if address_book_length== 0:
                print("Nothing to edit.\n")
                continue
            elif address_book_length == 1:
                selection = 0
            else:
                try:
                    selection = input(f"Enter record number [1 - {address_book_length}]: ")
                except KeyboardInterrupt or EOFError:
                    print("\nOperation calceled.\n")
                    continue

                if not selection.isnumeric():
                    print("Error: invalid input.\n")
                    continue
                else:
                    selection = int(selection) - 1
                    if selection < 0 or selection >= address_book_length:
                        print("Error: invalid record number.\n")
                        continue
                print("")

            record = menus.record(address_book[selection])
            if record:
                address_book[selection] = record
        elif selection == 5:
            search = menus.record(search=True)
            if search:
                menus.index(address_book, search, True)
        elif selection == 6:
            break