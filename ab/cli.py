from . import utils
from . import menus

def cli(addressBook):
    """
    Basic CLI implementation.
    """
    
    while True:
        selection = menus.main()

        if selection == 1:
            sort = menus.yes_no("Sort by first name?")
            if sort:
                utils.sort(addressBook, lambda a, b: a.first_name < b.first_name)
            else:
                sort = menus.yes_no("Sort by last name?")
                if sort:
                    utils.sort(addressBook, lambda a, b: a.last_name < b.last_name)
                else:
                    print("\nOperation calceled.\n")
        elif selection == 2:
            search = menus.record(search=True)
            if search:
                menus.index(addressBook, search)
        elif selection == 3:
            record = menus.record()
            if record:
                addressBook.append(record)
        elif selection == 4:
            abLen = len(addressBook)
            if abLen== 0:
                print("Nothing to edit.\n")
                continue
            elif abLen == 1:
                selection = 0
            else:
                try:
                    selection = input(f"Enter record number [1 - {abLen}]: ")
                except KeyboardInterrupt or EOFError:
                    print("\nOperation calceled.\n")
                    continue

                if not selection.isnumeric():
                    print("Error: invalid input.\n")
                    continue
                else:
                    selection = int(selection) - 1
                    if selection < 0 or selection >= abLen:
                        print("Error: invalid record number.\n")
                        continue
                print("")

            record = menus.record(addressBook[selection])
            if record:
                addressBook[selection] = record
        elif selection == 5:
            search = menus.record(search=True)
            if search:
                menus.index(addressBook, search, True)
        elif selection == 6:
            break