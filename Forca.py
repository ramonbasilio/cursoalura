def jogar():
    print("*******************")
    print("***Jogo da Forca***")
    print("*******************\n")

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        index = 0   #variável para mostrar a posição da letra contida na palavra secreta
        chute = input("Qual letra?")    #usuário insere uma letra para verificar se a letra está contida na palavra secreta
        chute = chute.strip()

        for letra in palavra_secreta:
            if(letra.upper() == chute.upper()):
                print("Encontrada a letra {} na posição {}".format(chute, index))
            index = index + 1


        print("jogando...")


    print("Fim do jogo")

if (__name__ == '__main__'):
    jogar()
