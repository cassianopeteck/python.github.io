"""

do while

Código para adivinhar um número



"""


"""palpite = 0
numero = 7


while True: # substituido != numero, bool(palpite) is
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == numero: #Estamos verificando nosso código
        print("Parabéns você acertou")
        break
    else: print("Você errou")
else:
    print("Erro na execução")
    print(bool(palpite))"""

    # Python code below
# Use print("messages...") to debug your solution.
# Python code below
# Use print("messages...") to debug your solution.

"""def find_largest(numbers):
    maior = 0
    for numero in numbers:
            if(maior < numero):
                maior = numero
    return maior

print(find_largest([7,17,13,19,51]))"""

from asyncio.windows_events import NULL
from logging import NullHandler
import sys
import math
from contextlib import redirect_stdout

def compute_closest_to_zero(ts):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    min_temperature = 0
    for minimo in ts:
        if minimo > 0:
            if min_temperature > 0:
                if min_temperature < minimo:
                    min_temperature = minimo
            elif min_temperature < 0:
                if (minimo < abs(min_temperature)):
                    min_temperature = minimo
        elif minimo < 0:
            if min_temperature > 0:
                if(min_temperature < abs(minimo)):
                    min_temperature = minimo
            elif min_temperature < 0:
                if abs(minimo) < abs(min_temperature):
                    min_temperature = minimo
    return min_temperature


print(compute_closest_to_zero([1,2,3,-5,-6]))