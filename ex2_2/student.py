from person import Person


class Student(Person):
    def __init__(self, name, street, city, state, country, complement, zipcode):
        super().__init__(name, street, city, state, country, complement, zipcode)
