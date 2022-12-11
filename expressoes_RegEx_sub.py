import re # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.sub(" ", "-" ,texto) # SUBSTITUI O QUE VOCÊ DIGITAR POR UM NOVO CARACTER INFORMADO POR VOCÊ,
# RETORNA JÁ MODIFICADO, PODENDO MODIFICAR DE NOVO
res = re.sub(",", ":" ,texto)

print(res) # RETORNA UMA LISTA, O QUE POSSIBILITA O COMANDO DO TIPO A SEGUIR: