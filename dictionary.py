carro={
    "Fabricante": "Honda",
    "Modelo": "HRV",
    "Ano": "2016",
    "Cor": "Prata"
    } #dictionary

#   KEY: VALOR --> RESGATAMOS PELA KEY
# MÉTODOS PARA OBTER ALGOESPECÍFICO:

fabricante = carro["Fabricante"]
#ou
fab = carro.get("Fabricante")

#ALTERAR:
carro["Cor"]="Preto"

#EXEMPLO COM FOR
for x in carro:
    print(x) #IMPRIMIR AS CHAVES

for x in carro:
    print(carro[x]) #IMPRIMIR OS VALORES

#USANDO 2 VARIÁVEIS
for k,v in carro.items(): # declara k e v, e os relacionam com os .items() do dictionary
    print(k + ": " + v) # pega tudo

# PEGAR TAMANHO
tam = len(carro) # tamanho retorna inteiro

# IF's
if "Modelo" in carro:
    print("Sim, 'Modelo' é uma chave")

# ADICIONANDO ITENS
carro["Cambio"] = "Automático"

# EXCLUIR ITEM
carro.pop("Cambio")
#ou
del carro["Cambio"]

#EXCLUIR TUDO
carro.clear()

# DICTIONARY DENTRO DE OUTRO DICTIONARY:

carros={
    "Carro1": {
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },
    "Carro2": {
        "Fabricante": "Volkswagem",
        "Modelo": "Golf"
    },
    "Carro3": {
        "Fabricante": "For",
        "Modelo": "Focus"
    }
}

print(carros["Carro1"]["Fabricante"]) # IMPRIMIR UM ESPECÍFICO

# OUTRO EXEMPLO

Carro1={
    "Fabricante": "Honda",
    "Modelo": "HRV"
}
Carro2={
    "Fabricante": "Volkswagem",
    "Modelo": "Golf"
}
Carro3={
    "Fabricante": "For",
    "Modelo": "Focus"
}

todos_carros = {
    "C1", Carro1,
    "C2", Carro2,
    "C3", Carro3
}

print(todos_carros["C1"]["Modelo"])