"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar):
        """Recebe o array com o conteudo a ser ordenado"""
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        array_ordenando = self.array_para_ordenar
        not_ordenado = True
        while not_ordenado:
            not_ordenado = False
            for index in range(len(array_ordenando) - 1):
                if array_ordenando[index] > array_ordenando[index + 1]:
                    array_ordenando.insert(index, array_ordenando.pop(index + 1))
                    not_ordenado = True
                
        self.array_ordenado = array_ordenando
        return array_ordenando

    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        string = ""
        for index in range(len(self.array_ordenado)):
            string += str(self.array_ordenado[index])
            if index != len(self.array_ordenado) - 1:
                string += ","
        
        return string
    
ordenar = Ordenacao([1, 4, 5, 6, 2])
ordenar.ordena()
print(ordenar.toString())