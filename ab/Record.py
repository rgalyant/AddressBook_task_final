class Record:
    """
    Class for containing record data.
    """

    __slots__ = ("first_name", "last_name", "phone", "address", "date_of_birth")

    def __init__(self, first_name, last_name, phone, address=None, date_of_birth=None):
        # Required
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

        # Optional
        self.address = address
        self.date_of_birth = date_of_birth