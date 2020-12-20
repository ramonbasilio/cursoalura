import Adivinhação
import Forca

print("**********************")
print("***Escolha seu jogo***")
print("**********************\n")

print("Forca (1) - Adivinha (2)")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando forca")
    Forca.jogar()

elif(jogo == 2):
    print("Jogando Adivinhação")
    Adivinhação.jogar()