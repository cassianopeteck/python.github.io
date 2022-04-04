#with open('./receitas/brigadeiro.txt', 'w') as arquivo: #se não especificar se é r (readable) ou w (writeable) não funcionará o código
 #   arquivo.write("imaginação")

"""arquivo = open('./receitas/brigadeiro.txt', 'w')
arquivo.write("padaria Yuyu")
arquivo.close()"""

"""with open('./receitas/brigadeiro.txt', 'a') as a: # a signfica append (adicionar ao final)
    a.write("Imaginacao")
    a.write("Padaria da Yuyu")
    a.write("\nA Padaria para todas as pessoas")
#    a.close"""

import os

#os.mkdir('D:\DankiCode\PythonClasses\Teste')
#os.mknod('D:\DankiCode\PythonClasses\Teste\teste.py')

#arquivo = open('.\Teste\teste.py')
arquivo = open('.\Teste\')
#print(arquivo = open('.\Teste\teste.py'))
#arquivo.write("teste ola mundo!")
#arquivo.close()

"""import pydf

pdf = pydf.generate_pdf("<h1>Ola Mundo!</h1><p>\nTestando meu primeiro documento pdf criado</p>")

with open('./receitas/meuarquivo.pdf','wb') as arquivo: #w(writeable) e b(arquivo binário)
    arquivo.write(pdf)"""