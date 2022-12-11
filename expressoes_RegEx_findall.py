import re # RegEx

# retorna lista contendo todas as ocorrências que encontrar em uma string

texto = "Curso de Python do CFB Cursos, canal do Youtube"

pesquisa=input("Pesquisar: ")

# res = re.findall("o", texto) # pesquisar 'Python' na variável texto
res = re.findall(pesquisa, texto) # pesquisar o input na variável texto

print(res)

qtde = len(res)

print("Quantidade: " + str(qtde))

for t in res:
    print(t)