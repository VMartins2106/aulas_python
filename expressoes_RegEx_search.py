import re # RegEx

texto = "Curso de Python do CFB Cursos, canal do Youtube"

res = re.search("Python", texto) # SEARCH cCONSEGUE DESCOBRIR AS POSIÇÕES DE ALGO

if res != None:

    posicao_inicial = res.start()
    posicao_final = res.end()
    tamanho = posicao_final - posicao_inicial

    print("Posição inicial: " + str(posicao_inicial))
    print("Posição final: " + str(posicao_final))
    print("Tamanho: " + str(tamanho))
else:
    print("Não encontrado")