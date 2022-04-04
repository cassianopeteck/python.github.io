import platform #importando biblioteca plataforma para identificar o sistema operacional
import os #importando biblioteca de manipulação de arquivos e diretórios
import datetime #biblioteca de leitura do tempo e data real

"""


"""
dataAtual = datetime.date.today()
anoAtual = dataAtual.strftime("%y")
mesAtual = dataAtual.strftime("%m")
diaAtual = dataAtual.strftime("%d")
mes = 0
idade = 0

if __name__ == '__main__':
    so = platform.system() #identificando qual é o sistema operacional
    if so == "Windows":
        
        os.mkdir('D:/DankiCode/PythonClasses/grupoRisco')
        print("Vá até a pasta grupoRisco e crie o arquivo registro.txt")
        
        def dadosPaciente():
            cadastroPaciente = {}
            = input("Digite o nome completo do paciente ")
            e_mail = input("Digite o e-mail do paciente ")
            cPF = int(input("Digite o CPF do paciente "))
            rG = int(input("Digite o RG do paciente "))
            fone = int(input("Digite o telefone do paciente "))
            diaNascimento = int(input("Digite a dia de nascimento do paciente "))
            mesNascimento = int(input("Digite a mes de nascimento do paciente "))
            anoNascimento = int(input("Digite a ano de nascimento do paciente "))
        
        idade = anoNascimento - anoAtual
        mes = mesNascimento - mesAtual 
        
        texto = f"""
        {nomeCompleto}, {e_mail}, {cPF}, {rG}, {fone},
        {diaNascimento}/{mesNascimento}/{anoNacimento}
        """

        if idade >= 65 and mes > 0:
            with open('D:/DankiCode/PythonClasses/grupoRisco/registro.txt','w') as reg:
                reg.write(texto, ", grupo de risco")
                reg.close()
        else:
            with open('D:/DankiCode/PythonClasses/grupoRisco/registro.txt','w') as reg:
                reg.write(texto)
                reg.close()
    print(texto, " e cheque o arquivo criado pelo sistema: ")
    if input("Digite se quer registrar mais um paciente: (S/n)") == "S":


    elif so == "Linux":
        
        os.mkdir('/home/grupoRisco')
        os.mknod('/home/grupoRisco/registro.txt')
        
        nomeCompleto = input("Digite o nome completo do paciente ")
        e_mail = input("Digite o e-mail do paciente ")
        cPF = int(input("Digite o CPF do paciente "))
        rG = int(input("Digite o RG do paciente "))
        fone = int(input("Digite o telefone do paciente "))
        diaNascimento = int(input("Digite a dia de nascimento do paciente "))
        mesNascimento = int(input("Digite a mes de nascimento do paciente "))
        anoNascimento = int(input("Digite a ano de nascimento do paciente "))

        idade = anoNascimento - anoAtual
        mes = mesNascimento - mesAtual 

        texto = f"""{nomeCompleto}, {e_mail}, {cPF}, {rG}, {fone}, 
        {diaNascimento}/{mesNascimento}/{anoNacimento}"""

        if idade >= 65 and mes > 0:
            with open('/home/grupoRisco/registro.txt','w') as reg:
                reg.write(texto, ", grupo de risco")
                reg.close()
        else:
            with open('D:/DankiCode/PythonClasses/grupoRisco/registro.txt','w') as reg:
                reg.write(texto)
                reg.close()
        print(texto, " e cheque o arquivo criado pelo sistema: ")
        if input("Digite se quer registrar mais um paciente: (S/n)") == "S":
    
    
    elif so == "MacOS":
        
        os.mkdir('/home/grupoRisco')
        os.mknod('/home/grupoRisco/registro.txt')
        
        nomeCompleto = input("Digite o nome completo do paciente ")
        e_mail = input("Digite o e-mail do paciente ")
        cPF = int(input("Digite o CPF do paciente "))
        rG = int(input("Digite o RG do paciente "))
        fone = int(input("Digite o telefone do paciente "))
        diaNascimento = int(input("Digite a dia de nascimento do paciente "))
        mesNascimento = int(input("Digite a mes de nascimento do paciente "))
        anoNascimento = int(input("Digite a ano de nascimento do paciente "))

        idade = anoNascimento - anoAtual
        mes = mesNascimento - mesAtual 

        texto = f"""{nomeCompleto}, {e_mail}, {cPF}, {rG}, {fone}, 
        {diaNascimento}/{mesNascimento}/{anoNacimento}"""

        if idade >= 65 and mes > 0:
            with open('/home/grupoRisco/registro.txt','w') as reg:
                reg.write(texto, ", grupo de risco")
                reg.close()
        else:
            with open('D:/DankiCode/PythonClasses/grupoRisco/registro.txt','w') as reg:
                reg.write(texto)
                reg.close()
        print(texto, " e cheque o arquivo criado pelo sistema: ")
        if input("Digite se quer registrar mais um paciente: (S/n)") == "S":