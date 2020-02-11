import random


def jogar():
    
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um número entre 1 e 100:")
        print("você digitou ", chute)

        if (int(chute) < 1 or int(chute) > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = int(chute) == numero_secreto
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! o  seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! o  seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - int(chute))
            pontos = pontos - pontos_perdidos

        print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()

