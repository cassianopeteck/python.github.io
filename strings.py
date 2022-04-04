"""#       0123456
nome = "chicago"
nome2 = "queens"
print(nome, end="@")
print(nome2)

for x in nome2:
    print(x , end="#")


lista = ["chicago",'salvador','queens', 'pernambuco']
print(lista)

lista2 = ['2','3','7','8','10']
print(lista2)

lista3 = [2.0,3.5,6.3]
print(lista3)

lista4 = [True,False]
print(lista4)

lista5 = [True, 'chicago', 2.5, False, 4]
print(lista5)

print(type(lista5))
print(lista5[2])

print(lista5[1:])
print(lista5[3:])
print(lista5[:2]) #último elemento menos 1
print(lista5[::])
print(lista5[:5 ])
print(lista5[1:5:2])
print(lista5[1:5:1])

print(len(lista5))
print(len(lista2))

print(sum(lista3))
print(max((lista3)))
print(min(lista3))

mainer = "Curso de python"
reniam = range(20)

print(mainer)
print(reniam)

lista6 = list(mainer)
lista7 = list(reniam)

print(lista6)
print(lista7)

elemento = 8

if elemento in lista7:
    print("Elemento escolhido está nesta lista")"""

"""texto = "carro, avião, trem, moto"
lista8 = list(texto)
print(lista8)

texto = texto.split(",")
print(texto)

lista8 = list(texto)
lista8.append("barco")
print(lista8)

for x in range(len(lista8)):
    print(x , lista8[x])

print(len(lista8))"""

"""trecho = "4 , World , Mario , Luigi , Peach"
lista9 = list(trecho.split(","))
print(lista9)

for x in range(len(lista9)):
    print("Hello, "+ lista9[x])

print(dir(map))"""

"""tudo o que tem na dir(str)
__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
  '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
  'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
  'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
  'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
  'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'"""

#frase = "Curso em video Python"
"""print(frase.__add__(" Jesus que dificil"))"""
"""print(frase.__class__(frase))"""
"""print(frase.capitalize())
print(frase.casefold())
print(frase.center(60))"""
#frase2 = frase.encode()
"""print(frase2)
print(frase.expandtabs())
print(frase.find("em"))
print("Ola, hoje temos o {}".format(frase).upper())
print("Ola, hoje temos o {}".format(frase).title())
print("Ola, hoje temos o {}".format(frase).strip())
"""
#frase3 = "Crystal1234"
"""print(frase3.isalnum())
print(frase3.isalpha())
print(frase3.isascii())
print(frase3.isdecimal())
print(frase.join(frase3))
print(frase3.encode())
print(frase.ljust(50))
print(frase3.ljust(50))"""
"""print(frase.split()) #
for x in frase.split():
    print(x)"""
"""print(frase.maketrans("me ajude com isto","Voce que se ajude"))"""
"""tudo o que tem em um dir(map):'__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__',
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__"""


input = """5
20 30 40 50 30
3
20 25 45
"""

x = input.split()
#print(input.split())
#print("-"*30)

#print(x)
#print("-"*30)

vendas = int(x[0])
mayor = int(x[vendas + 1])
#print(mayor)
#print("-"*30)
#print(vendas)
#print("-"*30)

sales = []
position = []
for i in range(1, len(x)-mayor-1):
    sales.append(int(x[i]))
for j in range(len(x)-mayor,len(x)):
    position.append(int(x[j]))


print(position)
print("-"*50)

#pos = sorted(sales, reverse=True)
print(pos)
print("-"*50)

init = 0
rank = 0
for x in sales:
    rank = x
    if x > rank:
         rank = x
         



"""total = []
for j, carlos in enumerate(position):
    for i, sale in enumerate(pos):
        if carlos > sale and i == 0:
            posicao = i + 1
            break
        elif carlos == sale:
            posicao = i + 1
            break
        else:
            posicao = i + 1
            break
    total.append(posicao)


print(total)"""