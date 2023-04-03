from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluir_livro(self, livro: Livro):
        if livro is None or not isinstance(livro, Livro):
            return

        if livro.codigo in [livro.codigo for livro in self.__livros]:
            return

        self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if livro is None or not isinstance(livro, Livro):
            return

        if livro.codigo not in [livro.codigo for livro in self.__livros]:
            return

        self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros
