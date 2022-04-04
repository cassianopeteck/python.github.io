 # maiúsculas e minúsculas
 # símbolos e espaços

"""
Security = chave
5ecur1ty = senha

hex
1 = 1
2 = 2 até o 9
10 = A
11 = B
12 = C
"""

chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"    
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    else: senha = senha + letra

print(senha)

"""
Exercício - Trocar variáveis
"""
#Trocando variáveis em python

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

#criaremos uma variável temporária

temp = x
x = y
y = temp

print(f"O valor de x após a troca: {x}")
print(f"O valor de y após a troca: {y}")

numero = float(input("Digite um número, maior, menor ou igual a zero e podendo ser decimal: "))

if numero > 0: print(f"O {numero} é maior que zero")
elif numero == 0: print(f"O {numero} é nulo")
else: print(f"O {numero} é menor que zero")