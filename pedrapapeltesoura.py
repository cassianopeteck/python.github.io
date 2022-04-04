#import random - se importar tudo do módulo random o programa ficará pesado então:
from random import choice


jogador_vitorias = 0
maquina_vitorias = 0

def opcao_jogador():
    esc_jogador = input("Escolha pedra, papel ou tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Opção inválida. Tente novamente")
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(["papel", "pedra", "tesoura"])
    return esc_maquina


while True :

    print("-"*30)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("-"*30)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador =="papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
                #jogador venceu
                print(f"Jogador ganhou!!! Voce escolheu {esc_jogador} e a maquina "
                    f"escolheu {esc_maquina}")
                jogador_vitorias += 1
    elif (esc_jogador == esc_maquina):
        print(f"Empatou!!! Voce escolheu {esc_jogador} e a maquina"
        f" escolheu {esc_maquina}")
        #empatou
    else:
        #Maquina ganha
        print(f"Voce perdeu!!! Voce escolheu {esc_jogador} e a maquina "
        f"escolheu {esc_maquina}")
        maquina_vitorias+=1

    print("-"*30)
    print(f"Vitorias do jogador: {jogador_vitorias}")
    print(f"Vitorias da máquina: {maquina_vitorias}")
    print("-"*30)
    
        
    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador in ["Sim", "sim", "s", "S", "SIM"] :
        pass
    elif esc_jogador in ["Nao", "NAO", "N", "n", "não", "NÃO"] :
        break
    else:
        break
