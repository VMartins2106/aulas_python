"""carros=["HRV", "Golf", "Focus", "Argo"] # ARRAY / LIST

print(carros[1])
carros[2]="Fusion"

for x in carros:
    print(x)"""

# ----------------NAS MATRIZES------------------------------
carros=[
    ["Modelo", "HRV"], 
    ["Fabricante", "Honda"],
    ["Ano", 2016]
    ]

# MANDAMOS IMPRIMIR NA LINHA [] COLUNA []
# A PRIMEIRA É SEMPRE A LINHA (HORIZONTAL) E A SEGUNDA É SEMPRE A LINHA (VERTICAL)

#EXEXMPLO: print(carros[0][0])

#USANDO UM FOR PARA IMPRIMIR TUDO

for l,c in carros:
    print("Linha: " + str(l) + " | " + "Coluna: " + str(c)) # TUDO DEVE ESTAR EM STRING, ENTÃO FAÇA A CONVERSÃO

#ALTERAR ALGO NA MATRIZ

carros[2][1] = 2019

#ADICIONAR ALGO NA MATRIZ

carros.append(["Cor", "prata"])