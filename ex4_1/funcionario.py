from cargo import Cargo
from pessoa import Pessoa
from dependente import Dependente


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, cargo: Cargo):
        super().__init__(nome, cpf)
        if not isinstance(cargo, Cargo):
            raise ValueError
        self.__cargo = cargo
        self.__dependentes = []

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: Cargo):
        if not isinstance(cargo, Cargo):
            raise ValueError
        self.__cargo = cargo

    @property
    def dependentes(self):
        return self.__dependentes

    def add_dependente(self, nome, cpf):
        if cpf in [dependente.cpf for dependente in self.__dependentes]:
            print("Dependente duplicado")
            return
        self.__dependentes.append(Dependente(nome, cpf))

    def rem_dependente(self, cpf):
        for dependente in self.__dependentes:
            if dependente.cpf == cpf:
                self.__dependentes.remove(dependente)

    def mostra_dados(self):
        super().mostra_dados()
        print(self.__cargo.descricao, self.__cargo.salario)
        [dependente.mostra_dados() for dependente in self.__dependentes]
