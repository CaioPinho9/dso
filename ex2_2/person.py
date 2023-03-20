from address import Address


class Person:
    def __init__(self, name, street, city, state, country, complement, zipcode):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError

        self._address = Address(street, city, state, country, complement, zipcode)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name=""):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, Address):
            self._address = address
        else:
            raise ValueError
