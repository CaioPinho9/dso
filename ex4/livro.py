from editora import Editora
from autor import Autor
from capitulo import Capitulo


class Livro:
    def __init__(
        self,
        codigo: int,
        titulo: str,
        ano: int,
        editora: Editora,
        autor: Autor,
        numero_capitulo: int,
        titulo_capitulo: str,
    ):
        if not isinstance(editora, Editora):
            raise ValueError
        if not isinstance(autor, Autor):
            raise ValueError
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__capitulos = [Capitulo(numero_capitulo, titulo_capitulo)]

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora: Editora):
        self.__editora = editora

    @property
    def autores(self):
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if autor is None or not isinstance(autor, Autor):
            return

        if autor.codigo in [autor.codigo for autor in self.__autores]:
            return
        self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor is None or not isinstance(autor, Autor):
            return

        if autor.codigo not in [autor.codigo for autor in self.__autores]:
            return

        self.__autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        capitulo = Capitulo(numero, titulo)

        if capitulo.titulo in [capt.titulo for capt in self.__capitulos]:
            return

        self.__capitulos.append(capitulo)

    def excluir_capitulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                self.__capitulos.remove(capitulo)

    def find_capitulo_by_titulo(self, titulo: str):
        for capitulo in self.__capitulos:
            if capitulo.titulo == titulo:
                return capitulo
