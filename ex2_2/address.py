from validate import validate_str


class Address:
    def __init__(self, street, city, state, country, complement, zipcode):
        validate_str(street, city, state, country, complement)
        self._street = street
        self._city = city
        self._state = state
        self._country = country
        self._complement = complement

        if isinstance(zipcode, int):
            self._zipcode = zipcode
        else:
            raise ValueError

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, street=""):
        if isinstance(street, str):
            self._street = street
        else:
            raise ValueError

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city=""):
        if isinstance(city, str):
            self._city = city
        else:
            raise ValueError
          
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state=""):
        if isinstance(state, str):
            self._state = state
        else:
            raise ValueError
          
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country=""):
        if isinstance(country, str):
            self._country = country
        else:
            raise ValueError
          
    @property
    def complement(self):
        return self._complement

    @complement.setter
    def complement(self, complement=""):
        if isinstance(complement, str):
            self._complement = complement
        else:
            raise ValueError
          
    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode=""):
        if isinstance(zipcode, int):
            self._zipcode = zipcode
        else:
            raise ValueError
