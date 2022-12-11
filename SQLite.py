import sqlite3
from sqlite3 import Error
import os

# NÃO EXECUTAR TUDO DE UMA VEZ SÓ !!!!!!!!!!!!!!

# IMPORTAMOS O SQLITE E O ERROR, PARA TRATAR ERROS

# CRIAR CONEXÃO COM O BANCO
def conexaoBanco():
    caminho="C:\\Users\\Win10\\Desktop\\python_vscode\\SQLite\\agenda.db"
    con = None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

# CRIAR TABELA
vsql = "CREATE TABLE tb_contatos(idContato INTEGER PRIMARY KEY AUTOINCREMENT,nomeContato VARCHAR(30),telefoneContato VARCHAR(14),emailContato VARCHAR(30));"

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

#--------------------------------------------------------------------------------

# INSERINDO INFORMAÇÕES - INSERT INTO

# AGORA ATRIBUI A 'VSQL' OUTRO CÓDIGO E CHAMA O MESMO SISTEMA
#EXEMPLO INSERINDO INFORMAÇÕES PRONTAS

vsql = "INSERT INTO tb_contatos(nomeContato, telefoneContato,emailContato) VALUES('Biel','11928716584', 'biel@gmail.com')"

def inserir(vcon,vsql):
    try:
        c = vcon.cursor()
        c.execute(vsql)
        vcon.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)

inserir(vcon, vsql)

#--------------------------------------------------------------------------------

#EXEMPLO INSERINDO INFORMAÇÕES PELO TECLADO

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
email = input("Digite o email: ")

vsql = "INSERT INTO tb_contatos(nomeContato, telefoneContato,emailContato)VALUES('"+nome+"','"+telefone+"', '"+email+"')"

def inserir(vcon,vsql):
    try:
        c = vcon.cursor()
        c.execute(vsql)
        vcon.commit()
        print("Registro inserido")
    except Error as ex:
        print(ex)

inserir(vcon, vsql)

#--------------------------------------------------------------------------------

#EXEMPLO DELETANDO INFORMAÇÕES

vsql = "DELETE FROM tb_contatos WHERE idContato=7"

# vsql = "DELETE FROM tb_contatos WHERE idContato=x" ASSIM, DELETA APENAS O USUÁRIO COM ID X

def deletar(vcon,vsql):
    try:
        c = vcon.cursor()
        c.execute(vsql)
        vcon.commit()
        print("Registro deletado")
    except Error as ex:
        print(ex)
    #FINALLY:  PODIA SER DESTE JEITO TAMBÉM
    #   print("Registro deletado")

deletar(vcon, vsql)

#--------------------------------------------------------------------------------

#EXEMPLO ALTERANDO INFORMAÇÕES

vsql = "UPDATE tb_contatos SET nomeContato='B',telefoneContato='11960586785', emailContato='b@gmail.com' WHERE idContato=6"

def alterar(vcon,vsql):
    try:
        c = vcon.cursor()
        c.execute(vsql)
        vcon.commit()
        print("Registro alterado")
    except Error as ex:
        print(ex)

alterar(vcon, vsql)

#--------------------------------------------------------------------------------

#EXEMPLO PARA VER INFORMAÇÕES - SELECT

vsql = "SELECT * FROM tb_contatos" # VER TODOS

# vsql = "SELECT * FROM tb_contatos WHERE idContato = 1" # VER POR ID
# vsql = "SELECT * FROM tb_contatos WHERE nomeContato = 'Victor'" # VER POR NOME
# vsql = "SELECT * FROM tb_contatos WHERE nomeContato LIKE '%o%'" # VER POR LIKE - CONTÉM 'o'
# vsql = "SELECT * FROM tb_contatos WHERE nomeContato LIKE 'B%'" # VER POR LIKE - COMEÇAM COM 'B'
# vsql = "SELECT * FROM tb_contatos WHERE nomeContato LIKE '%r'" # VER POR LIKE - TERMINAM COM 'r'

# vsql = "DELETE FROM tb_contatos WHERE idContato=x" ASSIM, DELETA APENAS O USUÁRIO COM ID X

def consulta(vcon,vsql):
    c = vcon.cursor()
    c.execute(vsql)
    #vcon.commit()  NÃO PRECISAMOS DOIS COMMIT, POIS É APENAS PARA ALTERAR ALGO
    # PORÉM PRECISAMOS GUARDAR O QUE FOI CONSULTADO EM UMA VARIÁVEL
    resultado=c.fetchall()
    return resultado

#GUARDAR TUDO EM 'RES'
res = consulta(vcon, vsql)
os.system('cls') # SÓ PARA ENXERGAR MELHOR
for r in res: # LAÇO FOR PARA IMPRIMIR TUDO QUE ESTIVER EM RES
    print(r)

#É NECESSÁRIO FECHAR A CONEXÃO APÓS USÁ-LA
vcon.close()