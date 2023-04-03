from pessoa import Pessoa


class Dependente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)

    def mostra_dados(self):
        super().mostra_dados()
