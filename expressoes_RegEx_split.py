import re # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.split(" ", texto) # ENCONTRAR DIVISÃO ENTRE CARACTERES A PARTIR DO CARACTER QUE VOCÊ QUISER
# res = re.split("\s", texto) TAMBÉM FUNCIONA

print(res) # RETORNA UMA LISTA, O QUE POSSIBILITA O COMANDO DO TIPO A SEGUIR:
print(res[2])

for t in res:
    print(t)