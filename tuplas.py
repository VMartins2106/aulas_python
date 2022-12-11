# GAMBIARRA PARA MODIFICAR UMA TUPLA

t_carros=("HRV", "Golf", "Argo")

l_carros=list(t_carros) # transforma a tupla em lista
l_carros[2] = "Focus" # altera a lista
t_carros=tuple(l_carros) # transforma a lista em tupla

for x in t_carros:
    print(x)

# A TUPLA NÃO SUPORTA MODIFICAÇÃO, JÁ A LISTA SIM