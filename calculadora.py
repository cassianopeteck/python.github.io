__doc__ = """Calculadora desenvolvida para realizar as operações 
simples como a sua semelhante do Windows



"""

import math


result: float

x = 0
y = 0
result = 0


def calculadora():
    __doc__ = """
    Aqui você consegue calcular a soma, subtração, multiplicação, divisão, elevar um número ao
    quadrado, fazer a inversão e a porcentagem de qualquer operação.
    
    """

    x = int(input("Insira as variáveis: "))
    op = input("Escolha: +, -, *, /, r(raiz quadrada), **(elevado ao quadrado),"
    " inv(1/x), % :")
    if op == "+":
        y = int(input("Insira as variáveis: "))
        result = x + y
        return print(result)
    elif op == "-":
        y = int(input("Insira as variáveis: "))
        result = x - y
        return print(result)
    elif op == "*":
        y = int(input("Insira as variáveis: "))
        result = x * y
        return print(result)
    elif op == "/":
        y = int(input("Insira as variáveis: "))
        result = x / y
        return print(result)
    elif op == "r":
        result = math.sqrt(x)
        return print(result)
    elif op == "**":
        result = x ** 2
        return print(result)
    elif op == "inv":
        result = 1/x
        return print(result)
    elif op == "%":
        return print(0)
    

calculadora()


"""from modulo import soma
from secundario import quadratica

print(soma(2, 3))

print(quadratica(5))"""