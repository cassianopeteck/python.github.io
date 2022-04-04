#paradigma imperativo
#imperare = comandar

#variáveis, atribuições e sequências
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

"""nome="Gabriel" #Variável global e deve ter 2 linhas de separação
#bloco externo


def minha_funcao():
    #Bloco interno "é conhecido como corpo(alma) da função"
    nome = "Ana" #variável local
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome=="Ana" :
        print("Impressão do bloco interno da condicao do IF")
    for x in tupla:
        print(x)



print(nome)
minha_funcao()

lista = [1, 2, 3, 4, 5 , 6]
print(lista)

retorno = lista.pop()
var1 = print("Ola mundo")
print(lista)
print("O retorno da função pop: ", retorno)
print("O retorno do print 'Ola mundo' eh: ", var1)

def ola_mundo():
    print("ola mundo")
    return ola_mundo


#retorno = ola_mundo()
#print(retorno)

def par_impar():
    numero = 5
    if (numero % 2) == 0:
        return "numero par"
    return "numero impar"

print(par_impar())


#Parametros de uma funcao

def myFunction(name): #parametro é o nome dado aos valores utilizados na definição da função
    # corpo da função
    print(name)



name = input("Qual seu nome? ")
myFunction(name)""" #argumento é o nome dado aos valores utilizados  na chamada de uma função
# se você definiu argumentos, isto não deve ser diferente do que você definiu

"""def imprimir_nomes(nome, sobrenome, idade):
    print('nome: ', nome)
    print('sobrenome: ', sobrenome)
    print('idade: ', idade)
    print("_"*50)


imprimir_nomes(sobrenome="Peteck", nome="Cassiano", idade=32) #se você não declarar desta forma e inverter
#os argumentos o código fará errado, pois os argumentos seguem a ordem da função acima"""

#argumento arbitrário *args - ele guarda os elementos dentro de uma tupla se 
#você não sabe quantos argumentos serão adicionados
"""def imprimir_nomes(nome=None, sobrenome=None, idade=None, *args):
    if nome!= None:
        print('nome: ', nome)
        print('sobrenome: ', sobrenome)
        print('idade: ', idade)
        print(*lista)
        print(type(lista))
        print("_"*50)
    else:
        print("Por favor, preencha seus dados")


lista = ["casado", "apaixonado pela noiva!"]
imprimir_nomes("Cassiano", "Peteck", 31, *lista)""" #parametros definidos são mais importantes do que parâmetros que não necessitam serem utilizados

#Argumentos arbitrários **Kwargs - Keywords arguments
#Esta função recebe argumentos que serão atribuídos em um dicionário

def print_names(**names):
    print(names)
    print(f"{names['names']} {names['uppernames']}")
    print(type(names))


print_names(names="Ana", uppernames ="Lúcia")