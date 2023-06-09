from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    """
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    """

    def valor_total_carta(self) -> int:
        soma = 0
        soma += self.__personagem.energia
        soma += self.__personagem.habilidade
        soma += self.__personagem.velocidade
        soma += self.__personagem.resistencia
        return soma

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
