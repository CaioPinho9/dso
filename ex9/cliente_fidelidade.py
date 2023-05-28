from cliente import Cliente


class ClienteFidelidade(Cliente):
    def __init__(self, codigo_fidelidade: int, desconto: float, cpf: str,
                 nome: str, endereco: str, telefone: str):
        self.__codigo_fidelidade = codigo_fidelidade
        self.__desconto = desconto
        super().__init__(cpf, nome, endereco, telefone)

    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade

    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade):
        self.__codigo_fidelidade = codigo_fidelidade

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto
