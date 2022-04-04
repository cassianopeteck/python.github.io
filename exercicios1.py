#01
print("Digite a área da base")
base = input()
print("Digite a altura")
high = input()
area = float(base) * float(high)
print(area)

#2
print("Digite o tamanho do lado de um quadrado?")
lado = input()
sqarea = float(lado)**2
print(sqarea)

#3
print("Digite o valor a pagar:")
Referencia = input()
print("Digite o desconto:")
desconto = input()
pagamento = float(Referencia)*(1 - float(desconto)/100)
print("O valor real a pagar será: ",+pagamento)

#4
print("Digite o diâmetro do círculo")
diam = input()
sqc1 = 3.1415 * ( float(diam)/2 )**2
print("A área do círculo é: ", +sqc1)

#5
print("Quanto custa 1 dólar?")
dolar = input()
print("Quanto você recebe em reais?")
reais = input()
dolarizou = float(reais)/float(dolar)
print("Você realmente recebe: ", +dolarizou)

#6
print ("Quanto você já chegou a receber em dólares?")
rela = input ()
realizou = float(rela)*float(dolar)
print("Você realmente recebeu isto em reais: ", +realizou)

