from autor import Autor
from editora import Editora
from biblioteca import Biblioteca
from livro import Livro


l = Livro(1, "", 1, Editora(1, ""), Autor(1, ""), 1, "aaaa")

b = Biblioteca()
b.incluir_livro(l)
b.excluir_livro(1)