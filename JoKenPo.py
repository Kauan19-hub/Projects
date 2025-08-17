import unicodedata
#Importe de biblioteca

from random import choice
#Importe de capacitação de escolhas

def remover_acentos(txt):
    return unicodedata.normalize('NFKD', txt).encode('ascii', 'ignore').decode('ascii')
    #Definição de variável para remover acentos

vitorias_jogador = 0
vitorias_maquina = 0
#Placares

def opcao_jogada():
#Definição opção jogada
    print("\nBem vindo ao Pedra, Papel e Tesoura!")
    print("-"*30)

#Escolhas do jodador
    jogador = input("\nEscolha entre pedra, papel ou tesoura: ").lower()
    if jogador in ["pedra", "papel", "tesoura"]:
        return jogador

    #Se a escolha não for nenhuma das 3 mencionadas, ele para e retorna o def para continuação
    else:
        print("\nOpção não identificada.")
        return opcao_jogada()

def opcao_maquina():
#Escolhas da máquina
    maquina = choice(["pedra", "papel", "tesoura"])
    return maquina

#Enquanto eu quiser jogar outra rodada...
while True:
    print("-" * 30)
    jogador = opcao_jogada()
    maquina = opcao_maquina()
    print("-" * 30)

    # Regras do jogo
    if (jogador == "pedra" and maquina == "tesoura") or \
       (jogador == "papel" and maquina == "pedra") or \
       (jogador == "tesoura" and maquina == "papel"):
        print(f"\nA máquina escolheu: {maquina}. O jogador ganhou!")

        vitorias_jogador += 1 #1 vitória a mais para o jogador se ele ganhar

    elif jogador == maquina:
        print(f"\nA máquina escolheu: {maquina}. O jogo empatou!") #Se empatar, o placar não muda
    else:
        print(f"\nA máquina escolheu: {maquina}. A máquina ganhou!")

        vitorias_maquina += 1 #1 vitória a mais para a máquina se ela ganhar

    # Placar
    print("-" * 30)
    print(f"\nPlacar do jogador: {vitorias_jogador}")
    print(f"Placar da máquina: {vitorias_maquina}")
    print("-" * 30)

    # Perguntar se deseja jogar novamente
    jogar_novamente = input("\nDeseja jogar novamente? (Sim/Não): ").strip().lower()
    jogar_novamente = remover_acentos(jogar_novamente)
    print("-"*30)

    #Se sim, continua...
    if jogar_novamente == "sim":
        print("\nÓtimo, vamos jogar mais uma rodada!")

    #Senão se for não, encerra...
    elif jogar_novamente == "nao":
        print("\nOk. O jogo está encerrado!")
        break

    #Senão, caso haja uma resposta não identificada, ele encerra
    else:
        print("\nResposta não identificada. Encerrando o jogo por segurança.")
        break