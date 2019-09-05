print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 31
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu número: ")
    print("você digitou ", chute)

    acertou = int(chute) == numero_secreto
    maior = int(chute) > numero_secreto
    menor = int(chute) < numero_secreto

    if(acertou):
        print("você acertou")
    else:
        if(maior):
            print("Você errou! o  seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! o  seu chute foi menor do que o número secreto.")

    print("Fim de jogo!")

    rodada = rodada + 1

