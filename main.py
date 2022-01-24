from ab import cli, AddressBook

if __name__ == "__main__":
    addressBook = AddressBook("ab.txt")
    addressBook.load()
    cli(addressBook)
    addressBook.save()