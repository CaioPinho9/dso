from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = defaultdict(list)
        self.__tipos_chamados = []

    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        return len(self.__chamados[tipo.codigo])

    # Permite incluir um novo chamado na lista de Chamados. O chamado incluido eh retornado como um Chamado
    # @param data data do chamado em formato Date
    # @param cliente referencia para o Cliente do chamado
    # @param tecnico referencia para o Tecnico do chamado
    # @param titulo titulo do chamado
    # @param descricao descricao do chamado
    # @param prioridade prioridade do chamado
    # @param tipo tipo do chamado (TipoChamado)
    # @return retorna o chamato cadastrado
    def inclui_chamado(
        self,
        data: Date,
        cliente: Cliente,
        tecnico: Tecnico,
        titulo: str,
        descricao: str,
        prioridade: int,
        tipo: TipoChamado,
    ) -> Chamado:
        if not isinstance(data, Date):
            return
        if not isinstance(cliente, Cliente):
            return
        if not isinstance(tecnico, Tecnico):
            return
        if not isinstance(tipo, TipoChamado):
            return
        
        for chamado in self.__chamados[tipo.codigo]:
            if (
                chamado.data == data
                and chamado.cliente.codigo == cliente.codigo
                and chamado.tecnico.codigo == tecnico.codigo
            ):
                return

        novo_chamado = Chamado(
            data, cliente, tecnico, titulo, descricao, prioridade, tipo
        )

        self.__chamados[tipo.codigo].append(novo_chamado)

        return novo_chamado

    # Permite incluir um novo TipoChamado na lista de Tipos de Chamado. O TipoChamado incluido eh retornado como um TipoChamado
    # @param codigo codigo do Tipo Chamado
    # @param nome nome do Tipo Chamado
    # @param descricao descricao do Tipo Chamado
    # @return retorna o Tipo Chamado cadastrado
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        for tipo_chamado in self.__tipos_chamados:
            if tipo_chamado.codigo == codigo:
                return

        novo_tipo_chamado = TipoChamado(codigo, descricao, nome)

        self.__tipos_chamados.append(novo_tipo_chamado)

        return novo_tipo_chamado

    # Retorna os tipos de chamado que foram cadastrados no controlador pelo metodo inclui_tipochamado
    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
