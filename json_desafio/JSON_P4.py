import json

with open("C:/Users/Win10/Desktop/python_vscode/json_desafio/JSON_exemplo.json") as f:
    # SELECIONAMOS ELE COM ESTE COMANDO, PUXANDO O PATH INTEIRO DELE
    jogador = json.load(f)
    # USA-SE 'LOAD' PARA ARQUIVO EXTERNO
    # USA-SE 'LOADS' PARA ARQUIVO INTERNO

# ISTO TAMBÉM FUNCIONA !!
# jogador = json.load("C:/Users/Win10/Desktop/python_vscode/JSON_exemplo.json")

# MANIPULANDO ARQUIVO EXTERNO (DO MESMO JEITO QUE O ANTERIOR, APENAS REFERENCIANDO EXTERNAMENTE):

# APENAS PRA SEPARAR E ENXERGAR MELHOR
def linha():
    print("-------------------------------------")

# CHAVES
for c in jogador:
    print(c)
linha()

# ITENS
for i in jogador.items():
    print(i)
linha()

# VALORES
for v in jogador.values():
    print(v)
linha()

# NOME JOGADOR
print(jogador["nome"])
linha()

# ITENS DA MOCHILA
for item in jogador["mochila"]:
    print(item)
linha()

# ITEMS UTILITÁRIOS
for a in jogador["utilitarios"]:
    print(a)
linha()

# TIPO EM ITEMS UTILITÁRIOS
for a in jogador["utilitarios"]:
    print(a["tipo"])
linha()

# TIPO E GENÉTICA EM ITEMS UTILITÁRIOS
for a in jogador["utilitarios"]:
    print(a["tipo"] + " - " + str(a["genetica"]))