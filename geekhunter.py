"""from turtle import position"""


"""def processInput ( input ):
    "Aqui você deve criar seu algoritmo para processar a entrada e depois retorna-la."

    vendas = input().split(" ")

    return position
"""
#Este e um exemplo de processamento de entradas (inputs), sinta-se a vontade para altera-lo conforme necessidade da questao.
"""value = input()
while (value):
    print(processInput(value))
    try:
        value = input()
    except EOFError:
        break"""


input = """5
20 30 40 50 30
3
10 15 25
"""

#print(input.split())
x = input.split()
print(x)
vendas = int(x[0])
mayor = int(x[vendas + 1])
#print(mayor)
#print(vendas)
total = 0
for i in range(1, len(x)-mayor-1):
    total[i-1] =x[i]
    print(total[i-1])


for i in range(len(x)-mayor,len(x)):
    print(i)



