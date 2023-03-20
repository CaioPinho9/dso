from person import Person
from student import Student


class Professor(Person):
    def __init__(self, name, street, city, state, country, complement, zipcode, student):
        super().__init__(name, street, city, state, country, complement, zipcode)

        if isinstance(student, Student):
            self._student = student
        else:
            raise ValueError

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student=Student("", "", "", "", "", "", 0)):
        if isinstance(student, Student):
            self._student = student
        else:
            raise ValueError
