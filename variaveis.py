# VARIÁVEIS GLOBAIS, QUE PODEM SER PEGAS EM QUALQUER PARTE DO PROJETO

num1=num2=res=0

def metodo():
    canal="CFP Cursos"
    print(canal)
    # 'CANAL' SÓ EXISTE DENTRO DESTE MÉTODO

def global_no_metodo():
    global teste
    teste="PRINT TESTE"

metodo()
global_no_metodo()
print(teste)

# DECLARAMOS ALGO COMO GLOBAL COM O COMANDO 'GLOBAL', PORÉM DEVEMOS CHAMAR O MÉTODO
