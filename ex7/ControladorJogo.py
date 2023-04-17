from AbstractControladorJogo import *


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__baralho = []
        self.__personagems = []

    """
    Retorna o baralho
    @return o baralho
    """

    @property
    def baralho(self) -> list:
        return self.__baralho

    """
    Retorna a lista de personagems
    @return a lista de personagems
    """

    @property
    def personagems(self) -> list:
        return self.__personagems

    """
    Permite incluir um novo Personagem na lista de personagens do jogo
    @param energia Energia do novo Personagem
    @param habilidade Habilidade do novo Personagem
    @param velocidade Velocidade do novo Personagem
    @param resistencia Resistencia do novo Personagem
    @param tipo TipoPersonagem (Enum) do novo Personagem.
    Deve ser utilizado TipoPersonagem.TIPO
    @return Retorna o Personagem incluido na lista
    """

    def inclui_personagem_na_lista(
        self,
        energia: int,
        habilidade: int,
        velocidade: int,
        resistencia: int,
        tipo: Tipo,
    ) -> Personagem:
        if not isinstance(tipo, Tipo):
            return
        psg = Personagem(energia, habilidade, velocidade, resistencia, tipo)
        self.__personagems.append(psg)
        return psg

    """
    Permite incluir uma nova Carta no baralho do jogo
    @param personagem Personagem da nova carta que sera incluida
    @return Retorna a Carta que foi incluida no baralho
    """

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        if not isinstance(personagem, Personagem):
            return
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    """
    Realiza uma jogada, ou seja:
    1. Recebe a mesa onde estao as cartas lancadas pelo Jogador 1
    e pelo Jogador 2
    2. Compara os valores totais das cartas dos jogadores que estao
    na mesa
    - O jogador que ganhar a rodada recebe a carta do jogador perdedor,
    sendo assim ele deve chamar o metodo inclui_carta_na_mao para as
    duas cartas que estao na mesa
    - Caso ocorra empate ambos os jogadores devem chamar o metodo
    inclui_carta_na_mao com suas respectivas cartas da mesa
    3.Ao final do metodo o jogador que estiver com a mao vazia
    perde o jogo (retornar o jogador vencedor). Caso ambos ainda tenham
    cartas na mao retorne None para indicar que ninguem venceu o jogo.
    @param mesa Mesa atual, contendo: Jogador 1, Jogador 2,
    Carta do Jogador 1 e Carta do Jogador 2
    @return Retorna o Jogador vencedor da rodada.
    Caso ocorra empate entre os jogadores, retorna None
    """

    def jogada(self, mesa: Mesa) -> Jogador:
        jogada_player1 = mesa.carta_jogador1.valor_total_carta()
        jogada_player2 = mesa.carta_jogador2.valor_total_carta()

        if jogada_player1 > jogada_player2:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador1
        elif jogada_player1 < jogada_player2:
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return mesa.jogador2
        else:
            mesa.jogador1.inclui_carta_na_mao(mesa.carta_jogador1)
            mesa.jogador2.inclui_carta_na_mao(mesa.carta_jogador2)
            return None
