print (30 * "-")

numero = int(input("Insira um nuhmero para descobrir se o mesmo eh primo "))

if numero > 1:
    for x in range (2, numero):
        if (numero % x) == 0: 
            print("Este não é um número primo")
            break
    else: 
        print("O nuhmero eh primo")
else:
    print("Esse nuhmero naho eh primo: Numero menor ou igual a 1")

print(30 * "-")

"""'Continue' é um comando para o caso de que eu queira pular uma condicional quando ela repete, e o 'Pass' 
serve para quando ocorre algum erro na sua condicional e você não consegue solucionar, daí você ignora 
utilizando este comando.
"""