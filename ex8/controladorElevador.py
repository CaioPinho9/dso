from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def subir(self) -> str:
        self.__elevador.subir()
        return "Saiu"

    def descer(self) -> str:
        self.__elevador.descer()
        return "Desceu"

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()
        return "Entrou"

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()
        return "Saiu"

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializar_elevador(
        self,
        andar_atual: int,
        total_andares_predio: int,
        capacidade: int,
        total_pessoas: int,
    ):
        if not isinstance(andar_atual, int):
            raise ComandoInvalidoException
        if not isinstance(total_andares_predio, int):
            raise ComandoInvalidoException
        if not isinstance(capacidade, int):
            raise ComandoInvalidoException
        if not isinstance(total_pessoas, int):
            raise ComandoInvalidoException
        if andar_atual < 0:
            raise ComandoInvalidoException
        if total_andares_predio < 0:
            raise ComandoInvalidoException
        if capacidade < 0:
            raise ComandoInvalidoException
        if total_pessoas < 0:
            raise ComandoInvalidoException
        if total_andares_predio < andar_atual:
            raise ComandoInvalidoException
        if capacidade < total_pessoas:
            raise ComandoInvalidoException

        self.__elevador = Elevador(
            andar_atual, total_andares_predio, capacidade, total_pessoas
        )
