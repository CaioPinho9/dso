class Cliente:
    def __init__(self, nome, fone):
        self.__nome = nome
        self.__fone = fone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome=""):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone=0):
        if isinstance(fone, int):
            self.__fone = fone
        else:
            raise ValueError
