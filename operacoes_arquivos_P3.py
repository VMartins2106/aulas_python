import re
import os

nome="teste46.txt"
caminho="C:/Users/Win10/Desktop/python_vscode/"
#f=open(caminho+nome,"x")
#f.close()

# ESTE SISTEMA IMPEDE DE CRIAR ALGO QUE JÁ EXISTE
if os.path.exists(caminho+nome):
    print("Arquivo existente")
else:
    f=open(caminho+nome,"x")
    f.close()
    print("Arquvio adicionado")

# IF E ELSE PARA REMOVER

if os.path.exists(caminho+nome):
    os.remove(caminho+nome) # ISTO INSERE O COMANDO NO CMD PARA EXCLUSÃO
    print("Arquvio removido")
else:
    print("Arquivo inexistente")
 
# DESTE JEITO ELE CRIA E JÁ DELETA, PORÉM TODOS OS COMANDOS FUNCIONAM SEPARADAMENTE