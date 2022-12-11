"""

ESTRUTURA BÁSICA DE UM TRY EXCEPTION

try

except

finally

""" 
x=1
try:
    print(x)
except:
    print("ERRO, não definido")

# ERROS CONHECIDOS

try:
    print(x)
except NameError:
    print("ERRO, não definido")
except:
    print("ERRO, desconhecido")

# TRY EXCEPT COM 'ELSE'

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")

# FUNCIONANDO NORMALMENTE

x=10

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo") # CAI AQUI SE DER CERTO

# TRY EXCEPT COM 'FINALLY'

try:
    print(x)
except:
    print("Erro no programa")
else:
    print("Tudo certo")
finally:
    print("Fim do tratamento") # EXECUTA ESTA LINHA INDEPENDENTE DE ONDE CAIR

# EXEMPLOS DE ERROS COM 'RAISE EXCEPCTION' --> PARA O PROGRAMA NA HORA COM UMA MENSAGEM PERSONALIZADA

num=-10
if num < 1:
    raise Exception("Valor não permitido") # 'raise Exception' funciona como relator personalizada de erro

# ----------------

num="Bruno"

if not type(num) is int:
    raise Exception("Valor não é inteiro")
else:
    print(str(num))