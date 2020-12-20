import random

def jogar():
    print("*******************")
    print("Jogo da adivinhação")
    print("*******************\n")

    #random.seed(10)
    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print("Escolha o nível de dificuldade")
    print("Fácil (1) - Médio (2) - Difícil (3)\n")

    nivel = int(input("Escolha o nível: "))
    print("")

    if (nivel == 1):
        total_de_tentativas = 20

    elif (nivel == 2):
        total_de_tentativas = 10

    elif (nivel == 3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100 \n")
            continue  # O Continue irá parar nessa iteração e voltar no 'for' na iteração seguinte

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print("Você acertou! Você fez {} pontos.\n".format(pontos))
            break # Ao chegar no Break sairá do looping

        else:
            if maior:
                print("Você errou! Seu chute foi MAIOR que o número secreto\n")
            elif menor:
                print("Você errou! Seu chute foi MENOR que o número secreto\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")
