import math

def maior():
    x = int(input("Digite um dos valores para a verificação: "))
    y = int(input("Digite um dos valores para a verificação: "))
    if x > y:
        return X
    else:
        return y


print(maior())

def media():
    x = int(input("Digite um dos valores para calcular a media: "))
    y = int(input("Digite um dos valores para calcular a media: "))
    media = (x+y)/2
    return media


print(media())

def exponencial():
    x = int(input("Digite o valor da base: "))
    y = int(input("Digite o valor do expoente: "))
    #expo = x**y
    expo = math.pow(x, y)
    return expo


print(exponencial())

