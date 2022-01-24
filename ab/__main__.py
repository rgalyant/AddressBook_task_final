"""
Module main function for standalone use.
"""

from .cli import cli
from .AddressBook import AddressBook

if __name__ == "__main__":
    address_book = AddressBook("ab.txt")
    address_book.load()
    cli(address_book)
    address_book.save()