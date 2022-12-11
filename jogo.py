import random
import os

os.system('cls')

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Informe seu palpite: "))

while sorteado != jogador:
    os.system('cls')
    if(sorteado>jogador):
        print("ERRO, o número é maior")
    elif(sorteado<jogador):
        print("ERRO, o número é menor")
    erros+=1
    jogador=int(input("Informe seu palpite: "))

print("Número " + str(jogador) + ", você acertou em " + str(erros+1) + " tentativas")