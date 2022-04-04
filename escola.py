from abc import ABC, abstractmethod


#Classe abstrata : não devemos fazer instância desta classe, como torná-la abstrata,além de obrigar que seus métodos sejam instanciados. 
class Pessoa(ABC):
    
    # Suplerclasse - classe mãe, classe pai

    def __init__(self, nome = None, data = None, cpf = None, rg = None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Executando o construtor da classe Pessoa")
    

    def imprimir_nome(self):
        return f"Estou retornando o valor armazenado na variavel nome: {self.nome}"


    @abstractmethod
    def trabalhar(self):
        #print("Trabalhando...")
        print("Implemente a funcionalidade deste método")


#Classes concretas - iremos criar instâncias destas classes/objetos
class Administrador(Pessoa):

    def trabalhar(self):
        return super().trabalhar()
        """nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Organizando planilhas...') #anteriormente return"""


#Classes concretas - iremos criar instâncias destas classes/objetos
class Professor(Pessoa):

    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []


    def trabalhar(self): #anteriormente lecionar
        nome_classe = self.__class__.__name__
        print(f'Classe {nome_classe} Ensinando...') #anteriormente return 


#Classes concretas - iremos criar instâncias destas classes/objetos
class Aluno(Pessoa):
    
    #Subclasse - classe filha, classe filha

    def __init__(self, nome):
        super().__init__(nome) #antigamente escrito como Pessoa e não preciso utilizar a variável self.
        self.matricula = None
        self.notas = []
        print("Classe Aluno")
        

    def estudar(self):
        return "Estudando..."


professor1 = Professor('Marcos')
administrador = Administrador('Joao')
administrador.trabalhar()
professor1.trabalhar()

#pessoa1 = Pessoa() consegui transformar a classe Pessoa em abstração


"""aluno1 = Aluno('Joseph')
print(aluno1.imprimir_nome())

professor1 = Professor('Marcos')
print(professor1.imprimir_nome())

administrador1 = Adminsitrador()
professor1.trabalhar()
administrador1.trabalhar()

print(type(aluno1))
print(type(professor1))

print(aluno1.estudar())
print(professor1.lecionar())

"""
"""@property
    def nome(self): #antigamente get_nome
        return self.__nome

    @nome.setter
    def nome(self, nome): #antigamente era o set_nome
        self.__nome = nome
    
    @property    
    def idade(self): #antigamente get_idade
        return self._idade

    @idade.setter
    def idade(self, idade): #antigamente set_idade
        self._idade = idade
"""

    
            
"""aluno1 = Aluno('Jose', 15, 123456)
print(aluno1.nome)
aluno1.nome = 'Joseph'
print(aluno1.nome)

print(aluno1.idade)
aluno1.idade = 27
print(aluno1.idade)
"""
"""print(aluno1.__matricula)
print(aluno1.__notas)
"""

"""
Conceito de getters e setters

Herança simples e herança múltipla, java não tem este conceito por isto usam o conceito de interface
Aumenta a relação entre classes, aumentando o acoplamento  


---
Polimorfismo - só existe polimorfismo se existe herança, e é a forma de executar o mesmo método de
diversas maneiras somente mudando as instruções de execução.

---
Classe abstrata -

---

Herança múltipla -
sugestão inicial: máximo de 4 níveis de herança 
"""