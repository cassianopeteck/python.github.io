# num = 5
# numero = 2

# print(5/2)


numero = int(input("Insira o número para descobrir se o mesmo é par: "))

if (numero % 2) == 0: print(f"{numero} eh um nuhmero par.")
else: print(f"{numero} eh um nuhmero ihmpar.")

# fatorial

fatorial = 0

produtorio = int(input("Digite o valor que será calculado o fatorial: "))

if produtorio < 0: print("Não existe fatorial de nuhmero negativo")
elif produtorio == 0: 
    fatorial = 1
else:
    while produtorio >= 1:
       fatorial = produtorio
       produtorio = produtorio - 1
       fatorial = fatorial * produtorio
       print(fatorial)
print(f"O resultado do teu fatorial é {fatorial}.")
