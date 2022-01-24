class Record:
    """
    Class for containing record data.
    """

    __slots__ = ("first_name", "last_name", "phone", "address", "date_of_birth")

    def __init__(self, first_name, last_name, phone,
        address = None, date_of_birth = None):
        
        # Required
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

        # Optional
        self.address = address
        self.date_of_birth = date_of_birth
    
    # For debugging purposes
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.address}, {self.date_of_birth}"