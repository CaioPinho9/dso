from pedido_duplicado_exception import PedidoDuplicadoException
from pedido import Pedido


class ControladorPedidos():
    def __init__(self):
        self.__pedidos = []

    @property
    def pedidos(self):
        return self.__pedidos

    def busca_pedido_por_numero(self, numero):
        for pedido in self.__pedidos:
            if pedido.numero == numero:
                return pedido
        return None

    def incluir_pedido(self, pedido):
        if not pedido:
            return None
        for pedido_existente in self.__pedidos:
            if pedido_existente.numero == pedido.numero:
                raise PedidoDuplicadoException()
        self.__pedidos.append(pedido)

    def excluir_pedido(self, numero):
        for index, pedido in enumerate(self.__pedidos):
            if pedido.numero == numero:
                return self.__pedidos.pop(index)
        return None

    def calcular_faturamento_pedidos(self, distancia, cpf):
        total = 0
        for pedido in self.__pedidos:
            if pedido.cliente.cpf == cpf:
                total += pedido.calcula_valor_pedido(distancia)

        return total
