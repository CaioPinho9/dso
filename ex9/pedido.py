from cliente import Cliente
from tipo_pedido import TipoPedido
from item_pedido import ItemPedido
from cliente_fidelidade import ClienteFidelidade


class Pedido():
    def __init__(self, numero: int, cliente: Cliente, tipo: TipoPedido):
        if not isinstance(numero, int):
            raise TypeError()
        if not isinstance(cliente, Cliente):
            raise TypeError()
        if not isinstance(tipo, TipoPedido):
            raise TypeError()
        self.__numero = numero
        self.__cliente = cliente
        self.__tipo = tipo
        self.__itens = []

    @property
    def numero(self):
        return self.__numero

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tipo(self):
        return self.__tipo

    @property
    def itens(self):
        return self.__itens

    @numero.setter
    def numero(self, numero):
        if not isinstance(numero, int):
            raise TypeError()
        self.__numero = numero

    @cliente.setter
    def cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError()
        self.__cliente = cliente

    @tipo.setter
    def tipo(self, tipo):
        if not isinstance(tipo, TipoPedido):
            raise TypeError()
        self.__tipo = tipo

    def inclui_item_pedido(self, codigo, descricao, preco):
        item_novo = ItemPedido(codigo, descricao, preco)
        for item in self.__itens:
            if item.codigo == codigo:
                return None
        self.__itens.append(item_novo)
        return item_novo

    def exclui_item_pedido(self, codigo):
        for index, item in enumerate(self.__itens):
            if item.codigo == codigo:
                return self.__itens.pop(index)
        return None

    def calcula_valor_pedido(self, distancia: float):
        total = 0
        for item in self.__itens:
            total += item.preco_unitario
        total += self.__tipo.fator_distancia * distancia
        if isinstance(self.__cliente, ClienteFidelidade):
            total *= 1 - self.__cliente.desconto
        return total
