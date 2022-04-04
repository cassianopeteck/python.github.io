# Paradigma imperativo


"""
Paradigma imperativo - foi a primeira forma que se pensou em representar o mundo real no mundo digital, desta 
forma surgiu o Fortran como exemplo clássico. Sequência - Decisão e a Iteração (laços de repetição), sem sintaxe definida
Paradigma Estruturado - C - apresentam sintaxe definida e estruturas repetição.
Paradigma procedural - Python

"""

def registro():
    paciente={'nome': nome, 'idade': idade, 'cpf': cpf, 'rg': rg, 'email': email }
    return paciente


#Reuso e coesão

"""
Classe - é a descrição de um objeto que tem características iguais/similares (CamelCase), ela consegue descrever
Objeto - o construtor cria os objetos
Construtor - é uma função com o mesmo nome da classe que a gente não cria e sim o Python, toda vez que
você chama o Objeto, o Python cria um novo Construtor com o mesmo nome da Classe.
Os Dander Objects são aqueles que criam o construtor dentro do Python.
Instanciando o objeto é passar o valor do Construtor para dentro de uma variável(que no paradigma orientado a objeto
é conhecido como atributos)
"""

#Paradigma procedural

"""Evento discreto, ele tem uma mudança de estado"""

class PacienteCovid:
    
    def __init__(self, nome, idade, cpf, email): #self é o construtor da mesma classe
        print("Acessei o Construtor")
        self.nome = nome #também conhecido como this em outras linguagens self (é o construtor).nome é o atributo, igual a variável
        self.idade = idade
        self.cpf = cpf
        self.email = email




"""
Diferença entre o paradigma procedural e o imperativo, principalmente suas características: Reuso, Coesão
Acoplamento, herança e polimorfismo, GAP Semântico

Simulação de eventos discretos - paradigma orientado à objetos
Relação - Destacando funções e variáveis
Não existe um objeto sem antes existir uma classe, não existe um jeito de excluir ou deletar um objeto
que é criado pelo Python.

Abstração é o processo pelo qual se isolam atributos de um objeto, considerando os que certos grupos de objetos
tenham em comum.
----

Conceitos Estruturais

-Classe

Classe é uma estrutura que abstrai um conjunto de objetos com características similares. Definindo o com-
portamento dos seus objetos através das estruturas.

1 - atributos
2 - métodos

A classe define um tipo de dado abstrato.

Reuso, não existe pior prática em programação do que repetir um código.
---
Objeto é a representação de um conceito/entidade do mundo real,
que pode ser física ou conceitual e possui um significado bem definido
para um determinado software.



Instâncias da classe conta
O parâmetro self pode ser mudado por outra palavra, porém
esta primeira palavra que representa os atributos da minha classe
deve ser a mesma para todos os atributos que estão sendo criados.

Há diferença entre um atributo de instância e um atributo de classe.

Atributo dinâmico é pertencente apenas a função ou classe que ele pertence
e não tem como usá-lo por outros atributos.



"""

