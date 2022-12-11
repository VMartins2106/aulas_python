texto="Curso de Python"
palavra="python"

res="Python" in texto # PERGUNTA SE AQUELE TEXTO ESTÁ NA VARIÁVEL 'TEXTO'
res="Python" not in texto # PERGUNTA SE AQUELE TEXTO NÃO ESTÁ NA VARIÁVEL 'TEXTO'
res=palavra not in texto # PERGUNTA SE A VARIÁVEL 'PALAVRA' NÃO ESTÁ NA VARIÁVEL 'TEXTO'
#RETORNAM VALORES BOOLEANOS, TRUE OU FALSE

#PARA EVITAR QUE, POR CONTA DE UMA LETRA MAIÚSCULA, RETORNE ALGO INDESEJADO, PODEMOS USAR:
res=palavra.upper() in texto.upper()

canal="CFB Cursos"
#CONCATENAÇÃO FUNCIONA ASSIM:
res=texto + " do canal " + canal

#EXEMPLO COM DIFERENTES TIPOS DE VARIÁVEIS
cidade="Caieiras"
dia=7
mes="Dezembro"
ano=2022
canal="CFB Cursos"

res=cidade + ", " + str(dia) + " de " + mes + " de " +str(ano)

#PARA FACILITAR O TRABALHO, PODEMOS FAZER ISSO:
data = "{}, {} de {} de {}" # INDICAMOS QUE NAQUELAS POSIÇÕES (CHAVES) IREMOS INSERIR VARIÁVEIS
#INSERIMOS AS VARIÁVEIS REFERENCIANDO A PRINCIPAL E COM '.format()', INSERINDO AS VARIÁVEIS
print(data.format(cidade,dia,mes,ano))

#PARA INSERIRMOS ENTER USAMOS O \n
data = "{}, {} de {} de {}\n{}"
print(data.format(cidade,dia,mes,ano, canal))

#PARA INSERIRMOS ASPAS À VARIÁVEL, DEVEMOS NOTIFICAR COM A CONTRA BARRA: 
data = "{}, {} de {} de {}\n\"{}\""
print(data.format(cidade,dia,mes,ano, canal))

# DE FORMA GERAL, TEMOS OS PRINCIPAIS:

# \' (APÓSTOFO)
# \" (ÁSPAS)
# \n (ENTER)
# \r (RETORNO DE CARGA)
# \t (TABULAÇÃO) -> TAB
# \b (BACKSPACE) -> APAGA CARACTER ANTERIOR