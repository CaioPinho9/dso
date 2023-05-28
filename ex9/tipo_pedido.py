class TipoPedido:
    def __init__(self, descricao: str, fator_distancia: float):
        self.__descricao = descricao
        self.__fator_distancia = fator_distancia

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not isinstance(descricao, str):
            raise TypeError()
        self.__descricao = descricao

    @property
    def fator_distancia(self):
        return self.__fator_distancia

    @fator_distancia.setter
    def fator_distancia(self, fator_distancia):
        self.__fator_distancia = fator_distancia
