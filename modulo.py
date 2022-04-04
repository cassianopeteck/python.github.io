#import random
#from random import random
"""from random import (
    random,
    choice,
    uniform
)"""
"""from random import(
    random as rd,
    choice as ch
)"""

from random import *
"""
#print(random.random())
#print(random())
print(rd())

lista = ["pedra", "papel", "tesoura"]
print(ch(lista))

for x in range(1, 9):
    print(x)"""

print(randint(1,5))

"""
Módulos - arquivos com extensão .py, ou seja,  arquivos python
Pacotes - diretórios contendo conjuntos de módulos - pastas com vários arquivos python

"""

def soma(a, b):
    return a + b

"""from pacote.sub_diretorio import outro as modulo

print(modulo.cubica(3))"""

"""#from pacote import principal
from pacote.principal import soma
from pacote.sub_diretorio.outro import cubica


#print(principal.soma(12,3))
print(soma(12,3))
print(cubica(6))"""

