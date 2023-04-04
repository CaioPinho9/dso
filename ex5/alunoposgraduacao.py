from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro: str):
        emprestimo_pos_grad = super().dias_de_emprestimo
        if self.__elaborando_tese:
            emprestimo_pos_grad *= 2

        return (
            super().emprestar(titulo_livro)
            + str(emprestimo_pos_grad)
            + " dias de prazo"
        )

    def devolver(self, titulo_livro: str):
        return super().devolver(titulo_livro)
