from .Record import Record

class AddressBook(list[Record]):
    """
    Class for containing address book data.
    """

    __slots__ = ("filename")

    def __init__(self, filename):
        self.filename = filename

    def save(self, filename=None):
        if not filename:
            filename = self.filename
        
        try:
            with open(filename, "wt") as file:
                for record in self:
                    file.write(f"{record.first_name}\n")
                    file.write(f"{record.last_name}\n")
                    file.write(f"{record.phone}\n")

                    if record.address or record.date_of_birth:
                        file.write(f"{record.address}\n")
                        file.write(f"{record.date_of_birth}\n")

                    file.write("RECORD_END\n")
        except OSError as ex:
            print("Failed to save data. Session is not saved.")
            print(ex)

    def load(self, filename=None):
        if not filename:
            filename = self.filename

        import os # Import only if necessary
        if not os.path.exists(filename) or not os.path.isfile(filename):
            return

        try:
            with open(filename, "rt") as file:
                buffer = []
                line_counter = 1
                while True:
                    line = file.readline()
                    if not line: break
                    line = line[:-1]
                    line_counter += 1

                    buffer_length = len(buffer)
                    if line == "RECORD_END":
                        if buffer_length == 5 or buffer_length == 3:
                            self.append(Record(*buffer))
                        else:
                            print(f"Corrupted record at line {line_counter} (marker encountered).")
                        buffer.clear()
                    elif buffer_length == 5:
                        print(f"Corrupted record at line {line_counter} (marker expected).")
                        buffer.clear()
                    else:
                        buffer.append(line)
                if len(buffer) > 0:
                    print(f"Corrupted last record.")
                    buffer.clear()
            print(f"Successfully loaded {len(self)} record(s)")
        except OSError as ex:
            print(f"Encountered error when trying to load file: {ex}")
