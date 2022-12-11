#INICIALIZAÇÃO DA VARIÁVEL DE CONTROLE
# while  ( #TESTE LÓGICO )
    #COMANDO 1
    #COMANDO 2
    #COMANDO 3
    #incremento, decremento ou controle da váriavel de controle

import os
os.system('cls') #LIMPAR A TELA



carros=["HRV", "Golf", "Argo", "Onix", "Focus"]

tamanho_carros = len(carros)
i = 0
while i<tamanho_carros:
    print(carros[i])
    i+=1 

    if(i>=5): # também podemos usar o break incrementado com algum teste para parar o loop
        break

print("\nFim do loop")

# OUTRO EXEMPLO ADICIONANDO COISAS A UMA LIST E IMPRIMINDO COM UM FOR

carros=[]
carro=input("Digite o nome do novo carro: ")
while carro!= "-1":
    carros.append(carro)
    carro=input("Digite o nome do novo carro: ")

os.system('cls')

for x in carros:
    print(x)