import os
import sqlite3
from sqlite3 import Error

def conexaoBanco():
    caminho="C:\\Users\\Win10\\Desktop\\python_vscode\\SQLite\\agenda_real.db"
    con = None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = conexaoBanco()

def query(vcon,sql):
    try:
        c=vcon.cursor()
        c.execute(sql)
        vcon.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Opreção realizada com sucesso!")

def consultar(vcon,sql):
    c=vcon.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res

def menuPrincipal():
    os.system('cls')
    print("1 - Inserir novo registro")
    print("2 - Deletar registro")
    print("3 - Atualizar registro")
    print("4 - Consultar registros")
    print("5 - Consultar registro por nome")
    print("6 - Sair")

def menuInserir():
    os.system('cls')
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    vsql="INSERT INTO tb_contatos (nomeContato,telefoneContato,emailContato) VALUES ('"+vnome+"', '"+vtelefone+"', '"+vemail+"')"
    query(vcon,vsql)

def menuDeletar():
    os.system('cls')
    vid = input("Digite o ID do registro a ser deletado: ")
    vsql = "DELETE FROM tb_contatos WHERE idContato="+vid
    query(vcon,vsql)

def menuAtualizar():
    os.system('cls')
    vid = input("Digite o ID do registro a ser alterado: ")
    r = consultar(vcon,"SELECT * FROM tb_contatos WHERE idContato="+vid)
    rnome = r[0][1]
    rtelefone = r[0][2]
    remail = r[0][3]
    vnome = input("Digite o nome: ")
    vtelefone = input("Digite o telefone: ")
    vemail = input("Digite o email: ")
    if len(vnome)==0:
        vnome=rnome
    if len(vtelefone)==0:
        vtelefone=rtelefone
    if len(vemail)==0:
        vemail=remail
    vsql="UPDATE tb_contatos SET nomeContato='"+vnome+"', telefoneContato='"+vtelefone+"', emailContato='"+vemail+"' WHERE idContato="+vid
    query(vcon,vsql)

def menuConsultar():
    os.system('cls')
    vsql="SELECT * FROM  tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcount=0
    for r in  res:
        # FORMATAÇÃO DO PRINT:
        # O 0,1,2,3 É O ÍNDICE, O '_' É PARA PREENCHER ESPAÇOS VAZIOS COM O UNDERLINE
        # O MENOR É PARA ESCREVER NA ESQUERDA, CASO SEJA '>' É PARA COMEÇAR NA DIREITA
        print("ID: {0:_<3} NOME: {1:_<30} TELEFONE: {2:_<14} EMAIL: {3:_<30}".format(r[0], r[1], r[2], r[3]))
        vcount+=1
        if vcount>=vlim:
            vcount=0
            os.system("pause")
            os.system('cls')
    print("-- FIM DA LISTA --")
    os.system('pause')


def menuConsultaNome():
    os.system('cls')
    vnome=input("Digite o nome: ")
    vsql="SELECT * FROM  tb_contatos WHERE nomeContato LIKE '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcount=0
    for r in  res:
        # FORMATAÇÃO DO PRINT:
        # O 0,1,2,3 É O ÍNDICE, O '_' É PARA PREENCHER ESPAÇOS VAZIOS COM O UNDERLINE
        # O MENOR É PARA ESCREVER NA ESQUERDA, CASO SEJA '>' É PARA COMEÇAR NA DIREITA
        print("ID: {0:_<3} NOME: {1:_<30} TELEFONE: {2:_<14} EMAIL: {3:_<30}".format(r[0], r[1], r[2], r[3]))
        vcount+=1
        if vcount>=vlim:
            vcount=0
            os.system("pause")
            os.system('cls')
    print("-- FIM DA LISTA --")
    os.system('pause')

opc = 0

while opc!=6:
    menuPrincipal()
    opc=int(input("Digite uma das opções: "))
    if opc==1:
        menuInserir()
    elif opc ==2:
        menuDeletar()
    elif opc ==3:
        menuAtualizar()
    elif opc ==4:
        menuConsultar()
    elif opc ==5:
        menuConsultaNome()
    elif opc ==6:
        os.system('cls')
        print("Programa finalizado!")
    else:
        os.system('cls')
        print("Opção inválida")
        os.system("pause")

vcon.close()
os.system("pause")