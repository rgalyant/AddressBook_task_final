"""
Module main function for standalone use.
"""

from .cli import cli
from .AddressBook import AddressBook

if __name__ == "__main__":
    addressBook = AddressBook("ab.txt")
    addressBook.load()
    cli(addressBook)
    addressBook.save()