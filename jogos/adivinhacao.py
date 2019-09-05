import random


print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 3
rodada = 1
print(numero_secreto)

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
        print("você acertou")
        break
    else:
        if(maior):
            print("Você errou! o  seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! o  seu chute foi menor do que o número secreto.")

    print("Fim de jogo!")

