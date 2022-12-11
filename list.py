carros=["HRV", "Golf", "Argo", "Focus"]
carros[3]="Fusion"

# INDICE COMEÇA EM 0 E TERMINA EM 1
#print(carros[0])

#PORÉM PODEMOS PEGAR O ULTIMO DE FORMA FÁCIL, INVERTENDO A ORDEM
#print(carros[-1])

#PARA FAZER ADIÇÃO DE ELEMENTOS NA LISTA USAMOS:
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

print(str(len(carros)) + " carros na lista")
print(carros)

#PARA REMOVER ALGO DA LISTA USAMOS:
carros.remove("Fusion")
#IRÁ REMOVER APENAS A QUE ESTIVER COM A MESMA STRING

#PARA REMOVER O ÚLTIMO ELEMENTO DA LISTA USAMOS:
carros.pop()

#PARA REMOVER UM ELEMENTO ESPECÍFICO DA LISTA USAMOS:
del carros[2]

#PARA REMOVER TODOS ELEMENTOS DA LISTA USAMOS:
carros.clear()

#PARA COPIAR A LISTA E GUARDAR EM OUTRA VARIÁVEL USAMOS:
carros_dois=list(carros)

#PARA FUNDIR DUAS LISTAS USAMOS:
carros_dois=["Fusca", "147", "Brasília", "Celta"]
carros_tres=carros+carros_dois