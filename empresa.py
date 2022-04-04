

class Funcionario:

    def trabalhar(self):
        print("Trabalhando")

    
class FrontEnd(Funcionario):

    def trabalhar(self):
        print("FrontEnd")


class BackEnd(Funcionario):

    def trabalhar(self):
        print("BackEnd")


class FullStack(FrontEnd, BackEnd):
    pass



ana = FullStack()
ana.trabalhar()
"""jose = FrontEnd()
marcos = BackEnd()

jose.trabalhar()
marcos.trabalhar()
"""

"""
Algoritmo MRO - resolve os conflitos que ocorrem quando se utiliza o método
de heranças múltiplas e ele executa de acordo com a ordem de atributos
"""