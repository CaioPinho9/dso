from categoria_produto import CategoriaProduto
from cliente import Cliente


class Produto:
    def __init__(
        self,
        codigo,
        descricao,
        categoria,
    ):
        self.__codigo = codigo
        self.__descricao = descricao
        if isinstance(codigo, CategoriaProduto):
            self.__categoria_produto = categoria
        else:
            raise ValueError

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo=0):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao=""):
        self.__descricao = descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto):
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = categoria_produto
        else:
            raise ValueError

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade=0):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario=0):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            raise ValueError

    def preco_total(self):
        return self.__preco_unitario * self.__quantidade
