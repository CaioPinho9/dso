from cargo import Cargo
from funcionario import Funcionario


c1 = Cargo(1000, "batata")
c2 = Cargo(500, "cenoura")

f1 = Funcionario("Rob", "000.000.000-00", c1)
f2 = Funcionario("Lob", "111.111.111-11", c1)
f3 = Funcionario("Dob", "222.222.222-22", c2)

f1.add_dependente("Bor", "333.333.333-33")
f1.add_dependente("Bol", "444.444.444-44")
f1.rem_dependente("333.333.333-33")


f1.mostra_dados()

print("----------------")

f2.mostra_dados()

print("----------------")

f3.mostra_dados()
