import sqlite3
from sqlite3 import Error
import os

banco="C:/Users/Win10/Desktop/python_vscode/interface_grafica/teste_agenda.db"

def conexaoBanco():
    con = None
    try:
        con=sqlite3.connect(banco)
    except Error as ex:
        print(ex)
    return con

def dql(query): # SELECT
    vcon=conexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): # INSERT, UPDATE, DELETE
    try:
        vcon=conexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)