import random
import os
from colorama import Fore, Back, Style

jogarNovamente = "s"
jogadas = 0
quemJoga = 2 # 2 -> JOGADOR // 1 -> CPU
maxJogadas = 9
vitoria = "n"
velha=[
    [" ", " ", " "], # 0,0, 0,1, 0,2
    [" ", " ", " "], # 1,0, 1,1, 1,2
    [" ", " ", " "]  # 2,0, 2,1, 2,2
]

def tela():
    global velha
    os.system('cls')
    print("    0   1   2")
    print("0: " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1: " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2: " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if(quemJoga==2 and jogadas<maxJogadas):
        try:
            l=int(input("Linha: "))
            c=int(input("Coluna: "))
            while velha[l][c] != " ":
                l=int(input("Linha: "))
                c=int(input("Coluna: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Jogada inválida")
            os.system('pause')
            
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if(quemJoga==1 and jogadas<maxJogadas):
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c] != " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2

def verificarVitoria():
    global vitoria
    global velha
    vitoria="n"
    simbolos=["X", "O"]
    for s in simbolos:
        vitoria="n"
        #VERIFICAR VITÓRIA EM LINHAS
        indice_linha=indice_coluna=0
        while indice_linha<3:
            soma=0
            indice_coluna=0
            while indice_coluna<3:
                if(velha[indice_linha][indice_coluna]==s):
                    soma+=1
                indice_coluna+=1
            indice_linha+=1
            if (soma == 3):
                vitoria="s"
                break
        if vitoria != "n":
            break
        #VERIFICAR VITÓRIA EM COLUNAS
        indice_linha=indice_coluna=0
        while indice_coluna<3:
            soma=0
            indice_linha=0
            while indice_linha<3:
                if(velha[indice_linha][indice_coluna]==s):
                    soma+=1
                indice_linha+=1
            indice_coluna+=1
            if (soma == 3):
                vitoria="s"
                break
        if vitoria != "n":
            break    
        #VERIFICAR VITÓRIA EM DIAGONAL 1    
        soma=0  
        indice_diagonal=0
        while indice_diagonal<3:
            if(velha[indice_diagonal][indice_diagonal]==s):
                soma+=1
            indice_diagonal+=1    
        if soma == 3:
            vitoria="s"
            break    
        #VERIFICAR VITÓRIA EM DIAGONAL 2
        soma=0
        indice_diagonal_linha=0
        indice_diagonal_coluna=2
        while indice_diagonal_coluna>=0:
            if(velha[indice_diagonal_linha][indice_diagonal_coluna]==s):
                soma+=1
                indice_diagonal_linha+=1
                indice_diagonal_coluna-=1   
        if soma == 3:
            vitoria="s"
            break   
    return vitoria

def redefinir():
    global jogadas
    global quemJoga
    global maxJogadas
    global vitoria
    global velha

    jogadas = 0
    quemJoga = 2 # 2 -> JOGADOR // 1 -> CPU
    maxJogadas = 9
    vitoria = "n"
    velha=[
        [" ", " ", " "], # 0,0, 0,1, 0,2
        [" ", " ", " "], # 1,0, 1,1, 1,2
        [" ", " ", " "]  # 2,0, 2,1, 2,2
    ]

def vitoriaManual():
    global velha
    global vitoria
    vitoria="n"
    if ((velha[0][0]=="X") and (velha[0][1]=="X") and (velha[0][2]=="X")) or ((velha[1][0]=="X") and (velha[1][1]=="X") and (velha[1][2]=="X")) or ((velha[2][0]=="X") and (velha[2][1]=="X") and (velha[2][2]=="X")):
        vitoria="sl"
        return vitoria
    elif ((velha[0][0]=="O") and (velha[0][1]=="O") and (velha[0][2]=="O")) or ((velha[1][0]=="O") and (velha[1][1]=="O") and (velha[1][2]=="O")) or ((velha[2][0]=="O") and (velha[2][1]=="O") and (velha[2][2]=="O")):
        vitoria="ssl"
        return vitoria
    elif ((velha[0][0]=="X") and (velha[1][0]=="X") and (velha[2][0]=="X")) or ((velha[0][1]=="X") and (velha[1][1]=="X") and (velha[2][1]=="X")) or ((velha[0][2]=="X") and (velha[1][2]=="X") and (velha[2][2]=="X")):
        vitoria="sc"
        return vitoria
    elif ((velha[0][0]=="O") and (velha[1][0]=="O") and (velha[2][0]=="O")) or ((velha[0][1]=="O") and (velha[1][1]=="O") and (velha[2][1]=="O")) or ((velha[0][2]=="O") and (velha[1][2]=="O") and (velha[2][2]=="O")):
        vitoria="ssc"
        return vitoria
    elif ((velha[0][0]=="X") and (velha[1][1]=="X") and (velha[2][2]=="X")) or ((velha[0][2]=="X") and (velha[1][1]=="X") and (velha[2][0]=="X")):
        vitoria="sd"
        return vitoria
    elif ((velha[0][0]=="O") and (velha[1][1]=="O") and (velha[2][2]=="O")) or ((velha[0][2]=="O") and (velha[1][1]=="O") and (velha[2][0]=="O")):
        vitoria="ssd"
        return vitoria
    else:
        vitoria = "n"
        return vitoria

while vitoria == "n":
    tela()
    jogadorJoga()
    cpuJoga()
    vit = vitoriaManual()
    if(vit=="sl"):
        print(Fore.YELLOW + "Vitória do X por linha" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()
    elif(vit=="ssl"):
        print(Fore.YELLOW+"Vitória do O por linha" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()
    elif(vit=="sc"):
        print(Fore.YELLOW+"Vitória do X por coluna" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()
    elif(vit=="ssc"):
        print(Fore.YELLOW+"Vitória do O por coluna" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()
    elif(vit=="sd"):
        print(Fore.YELLOW+"Vitória do X por diagonal" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()
    elif(vit=="ssd"):
        print(Fore.YELLOW+"Vitória do O por diagonal" + Fore.RESET)
        repetir = input("Deseja jogar novamente? [s/n]: ")
        if repetir=="s":
            redefinir()