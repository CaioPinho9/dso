import datetime
from controladorPessoas import ControladorPessoas
from controladorChamados import ControladorChamados
from cliente import Cliente
from tecnico import Tecnico
from tipoChamado import TipoChamado


cp = ControladorPessoas()
cc = ControladorChamados()

cp.inclui_cliente(1, "Jean")
cp.inclui_cliente(1, "Jean")
cp.inclui_cliente(2, "Jorge")

cc.inclui_chamado(1, Cliente("", 1), Tecnico("a", 2), "", "", 0, TipoChamado(3, "", ""))


print(cc.total_chamados_por_tipo(TipoChamado(3, "", "")))
