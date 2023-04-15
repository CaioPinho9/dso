from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    # @return retorna a lista de clientes
    @property
    def clientes(self) -> list:
        return self.__clientes

    # @return retorna a lista de tecnicos
    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

    # Permite a inclusao de um novo cliente na lista de clientes
    # @param codigo codigo do Cliente
    # @param nome nome do Cliente
    # @return retorna o cliente inserido
    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        for cliente in self.__clientes:
            if cliente.codigo == codigo:
                return

        novo_cliente = Cliente(nome, codigo)

        self.__clientes.append(novo_cliente)

        return novo_cliente

    # Permite a inclusao de um novo tecnico na lista de tecnicos
    # @param codigo codigo do tecnico
    # @param nome nome do tecnico
    # @return retorna o tecnico inserido
    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        for tecnico in self.__tecnicos:
            if tecnico.codigo == codigo:
                return

        novo_tecnico = Tecnico(nome, codigo)

        self.__tecnicos.append(novo_tecnico)

        return novo_tecnico
