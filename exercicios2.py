"""a = 5
b = 8

if b < a: print("b é maior que a")
print("Código fora do bloco if")

print("B") if b < a else print("A")"""


"""print("Digite a idade da pessoa")
idade = input()
if idade < 16: print("Menor")
elif idade > 18: print("Maior")
else idade >= 16 or idade <= 18: print("Emancipado")"""

"""foto de rosto, corpo inteiro, fundo neutro, calça e camiseta neutra, roupa neutra """

"""print("Qual a sua idade")
ageone = input()
if ageone >= 5 and ageone <= 7: print('Infantil A')
elif ageone >= 8 and ageone <= 10: print('Infantil B')
elif ageone >= 11 and ageone <= 13: print('Juvenil A')
elif ageone >= 14 and ageone <= 17: print('Juvenil B')"""

"""x = 5
y = 3

if y > x:
    print("y é maior que x")
else:
    print("y é menor ou igual a x")
print("código fora do bloco condicional")

print( y < x )

a = 0
while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f"a não é menor ou igual a 5. Valor de a: {a}")
"""

"""print("O resultado final de a: ", a)
print(a <= 5)"""

"""s = "pernambuco"

for m in s:
    print(m)

for n in range(6): # range (6) significa que começamos do 0 até termos 6 dígitos
    print(n)"""

#for x in range(2 , 18 , 5):
#   print(x)

idade = int(input("Digite a idade do referido: "))
if idade < 16: print("Cidadão é menor")
if idade >= 16:
    if idade < 18: print("Cidadão emancipado")
if idade >= 18: print("Cidadão em maioridade")

nadador = int(input("Informe a idade do nadador: "))

if nadador >= 5:
    if nadador <= 7: print("Infantil A")
if nadador >= 8:
    if nadador <= 10: print("Infantil B")
if nadador >= 11:
    if nadador <= 13: print("Juvenil A")
if nadador >= 14:
    if nadador <= 17: print("Juvenil B")