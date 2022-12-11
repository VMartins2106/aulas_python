import json

# TRANSFORMANDO JSON EM PYTHON E MANIPULANDO ELE

jogador_json='{"nome": "Victor","time": "bodybuilder","vivo": "True","energia": "100","mochila": ["creatina", "whey", "albumina", "pre-treino"],"utilitários":[{"tipo": "crescimento", "genetica": 80},{"tipo": "emagrecimento", "genetica": 50},{"tipo": "ectomorfo", "genetica": 90}]}'
# ARQUIVO JSON DEVE FICAR NA MESMA LINHA

jogador=json.loads(jogador_json)

# CHAVES
for c in jogador:
    print(c)

# ITENS
for i in jogador.items():
    print(i)

# VALORES
for v in jogador.values():
    print(v)

# NOME JOGADOR
print(jogador["nome"])

# ITENS DA MOCHILA
for item in jogador["mochila"]:
    print(item)

# ITEMS UTILITÁRIOS
for a in jogador["utilitários"]:
    print(a)

# TIPO EM ITEMS UTILITÁRIOS
for a in jogador["utilitários"]:
    print(a["tipo"])

# TIPO E GENÉTICA EM ITEMS UTILITÁRIOS
for a in jogador["utilitários"]:
    print(a["tipo"] + " - " + str(a["genetica"]))
    

