# f GERALMENTE É ABREVIATURA DE 'FILE', NO MEIO DOS DEV's


# ISTO TAMBÉM FUNCIONA
# nome="teste.txt" 
# f = open("C:/Users/Win10/Desktop/python_vscode/"+nome,"")

# SEGUINTES MODOS PARA ABERTURA DE ARQUIVO

# r - READ   - LEITURA
# a - APPEND - ANEXAR
# w - WRITE  - ESCREVER
# x - CREATE - CRIAR
# t - TEXO - NA FRENTE DE ALGUM DOS ANTERIORES
# b - BINÁRIO - NA FRENTE DE ALGUM DOS ANTERIORES

# ISTO TAMBÉM FUNCIONA
# nome="teste.txt" 
# f = open("C:/Users/Win10/Desktop/python_vscode/"+nome,"")

# CRIANDO ARQUIVO EM TEXTO
# SE NÃO TIVER ARQUIVO, O W CRIA JÁ PARA ESCREVER
f = open("C:/Users/Win10/Desktop/python_vscode/teste.txt", "at")

txt = input("Digite um texto: ")

f.write(txt+"\n")

#f.write("CFB Cursos \n")
#f.write("Curso de Python")

# FECHAR O ARQUIVO (NECESSÁRIO PARA TERMINAR A ALTERAÇÃO)

f.close()

