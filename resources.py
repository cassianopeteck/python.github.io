"""def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(100)"""

"""
1 - Checar se o nosso número não é igual a 0
2 - se ele não for igual a zero - reduzir em 1 unidade
Como procurar entender como é o uso de uma função recursiva, isto é,
qual é o caminho de ida e qual é o de volta
"""

"""def reduzirNumero(numeroInt):
    #print(numeroInt)
    if numeroInt > 0:
        #N - 1
        reduzirNumero(numeroInt - 1)
        print(numeroInt)


reduzirNumero(10)"""


def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero +1):
            fatorial *= x
        return fatorial 


print(fatorialS(6)) 

#fatorial com solução recursiva

def fatorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorialR(numero - 1)


print(fatorialR(int(input("Digite o valor que voce quer descobrir o fatorial: "))))

"""quando fazemos uso de uma função recursiva, precisamos responder dois critérios:
1) Critério de parada: determina quando a função deve parar, recursion error!
2) Parâmetro da chamada de recursividade: mudança do parâmetro para que a função chegue no fim


"""