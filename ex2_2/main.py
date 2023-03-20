from student import Student
from professor import Professor


aluno = Student(
    "Joaozinho",
    "Ruazinha",
    "Cidadezinha",
    "Estadinho",
    "Paisinho",
    "Complementinho",
    12312,
)
professor = Professor(
    "Robertinho",
    "Ruazinha",
    "Cidadezinha",
    "Estadinho",
    "Paisinho",
    "Complementinho",
    12314,
    aluno,
)

print(
    professor.name,
    professor.address.street,
    professor.student.name,
    professor.student.address.street,
)
