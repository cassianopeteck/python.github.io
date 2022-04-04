"""Escrever um programa que identifica dentre 5 valores qual o maior"""

"""print("Insira 5 valores aleatórios")
val1 = int(input("Valor 1: "))
val2 = int(input("Valor 2: "))
val3 = int(input("Valor 3: "))
val4 = int(input("Valor 4: "))
val5 = int(input("Valor 5: "))

check = val1

if check < val2: check = val2
if check < val3: check = val3
if check < val4: check = val4
if check < val5: check = val5

print(f"O maior valor verificado foi: {check}")
    
termos = int(input("Insira quantos termos você quer: "))
numerador = 480
denominador = 22

soma = numerador/2
for x in range(1 , termos + 1):
    soma = soma + (numerador - 5 * x)/(denominador + x)
print(soma)"""


membros = int(input("Quantos termos você quer nesta soma? "))
numerador1 = 1
denominador1 = 2
soma2 = numerador1 / denominador1

for x in range(1, membros):
    numerador1 = numerador1 + 2 ** x
    denominador1 = 2 * x + 21
    soma2 = soma2 + numerador1 / denominador1
print(soma2)


"""c = 340 / 1 + 3/40
for z in range(1, 4):
    c = c + (32 + ( z - 1 ))/(40 - z)
print(c)"""