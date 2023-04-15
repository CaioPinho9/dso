from abc import ABC, abstractmethod
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class AbstractControladorChamados(ABC):
    # Retorna o total de chamados registrados para o TipoChamado recebido como parametro
    # @param tipo TipoChamado
    # @return int com a quantidade total dos chamados daquele tipo
    @abstractmethod
    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str) -> TipoChamado:
        pass

    @property
    @abstractmethod
    def tipos_chamados(self):
        pass
