import re

nome="teste.txt"
f=open("C:/Users/Win10/Desktop/python_vscode/gerar_txt/"+nome,"rt")

print("\n" + f.read()) # LÊ E MOSTRA O QUE TEM LÁ

# LER APENAS OS 10 PRIMEIROS CARACTERES, POR EXEMPLO:
print("\n" + f.read(10))

#LER LINHA POR LINHA
print(f.readline())

# LER LINHA POR LINHA COM FOR
for l in f:
    print(l)
 
# TESTES COM RexEx  
res=re.sub(" ","-",f.readline())
f.close() # FECHAR PARA ABRIR NOVAMENTE, SÓ QUE ESCREVENDO
f=open("C:/Users/Win10/Desktop/python_vscode/gerar_txt/"+nome,"wt")
f.write(res)
f.close()
print(res)
