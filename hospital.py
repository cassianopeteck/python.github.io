from datetime import date

class Paciente:
    
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        """self.peso = peso
        self.altura = altura
        self. signo = signo"""

    @classmethod
    def idadeAnoNascimento(cls, nome, anoNascimento, cpf, email):
        #return cls(date.today().year - anoNascimento)
        idade = date.today().year - anoNascimento
        return Paciente(nome, idade, cpf, email)

class Medico:
    pass


"""paciente = Paciente('Lucia Ana', 31, '000.000.000-00','ana.lucia@gmail.com')
print(paciente.__dict__)
print(Paciente.idadeAnoNascimento(2001))
"""


paciente = Paciente.idadeAnoNascimento('Lucia',1957, '000.000.000-00','lucia@gmail.com')
print(paciente.__dict__)
print(paciente.idade)