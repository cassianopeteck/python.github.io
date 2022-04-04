"""
Visibilidade é um modificador  de acesso

private (privada) - restritiva - > define que os atributos e métodos só podem ser manipulados dentro da classe
protected (protegida) - intermediária -> define que os atributos e métodos só podem ser manipulados dentro da classe e nas subclasses (ou nas classes em que o atributo for herdado)
public (pública) - menos restritiva -> define que os atributos e métodos são acessíveis em qualquer lugar

Dica: começar a programaçãos dos atributos como private e a medida que o processo vai crescendo
definir se ele continua ou não restritivo.
Já com relação aos métodos é de forma inversa, você começa com public e depois pode ir mudando até chegar em private

---
Name Mangling é quando o python cria uma variável que consegue acessar o atributo privado/protegido
_Classe__atributo


"""



class Conta:

    """ Acoplamento é uma forma de quantidade/medir o quanto
    as nossas unidades de códigos estão relacionadas
    deve ser flexível, mas pode ser definido como forte ou fraco.
        """

    taxa = 0.5

    @classmethod
    def retornarCodigo(cls): #pode ser self, cls(class), ou qualquer coisa
        print('Codigo: 555')


    @staticmethod
    def retornarCodigoBanco():
        return '345'


    def __init__(self, numero, titular, saldo=2000):
        self._numero = numero #visibility protected
        self.titular = titular #visibility public
        self.__saldo = saldo #private visibility
        self.__historico = [saldo]
        """self.rg = rg
        self.peso = peso
        self.altura = altura
        self. signo = signo"""


    def saldo(self):
        print(f'Saldo: R$ {self.__saldo}')


    def transacao(self, saldo):
        self.__historico.append(saldo)


    def extrato(self):
        print('----Extrato----')
        print("Conta: ", self._numero)
        for saldo in self.__historico: #self.saldo -= Conta.taxa
            print(f'Saldo: R${saldo}')


    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)


    def sacar(self, retirado):
        self.__saldo -= retirado
        self.transacao(self.__saldo) 


    def transferencia(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

#Atributos da classe Conta

"""conta1 = Conta(123456,'Ana Lucia', 50000)
conta2 = Conta(654321,'Cassiano', 50000)

print(conta1.__dict__)
print(conta2.__dict__)

conta2.extrato()

conta1.signo = 'Cancer'

print(conta1.__dict__)
print(conta2.__dict__)

del conta1.signo

print(conta1.__dict__)

#Método da classe, precisa declarar um atributo
Conta.retornarCodigo()

#Método estático, não vai saber nada da classe, pois não precisa declarar um atributo
#Mais indicado utilizar este método pois ele não utiliza nada do que foi declarado na classe
print(Conta.retornarCodigoBanco()) #Convenção
print(conta2.retornarCodigoBanco())"""

conta1 = Conta(123,'Mona Lisa', 2300)
conta2 = Conta(345, 'Albert')

conta1.transferencia(2000, conta2)
conta1.saldo()
conta2.saldo()
conta2.transferencia(675.4, conta1)
conta2.extrato()
conta1.extrato()