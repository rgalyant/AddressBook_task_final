from ab import cli, AddressBook

if __name__ == "__main__":
    address_book = AddressBook("ab.txt")
    address_book.load()
    cli(address_book)
    address_book.save()