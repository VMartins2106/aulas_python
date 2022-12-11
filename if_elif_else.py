clima="Sol"
dinheiro=500
lugar=""

if clima=="Sol" or (dinheiro>=300 and dinheiro<=500):
    lugar="clube"
else:
    lugar="cinema"
print("Vou ao " +lugar)



"""if op=="+": # VERIFICA É VERDADEIRO ///// == PARA ATRIBUIÇÃO/COMPARAÇÃO
    res=a+b
elif op=="-": 
    res=a-b
elif op=="*": 
    res=a*b
elif op=="/": 
    res=a/b
else:
    print("Operador inválido")

print(str(a) + op + str(b) + " = " + str(res))"""

# O COMANDO PARA O ESLE IF NO PYTHON É 'ELIF'
# O ELSE SÓ É USADO PARA CASO TODOS OS ANTERIORES SEJAM FALSOS
# O OPERADOR 'E' NO PYTHON É O 'and' (ambos obrigatóriamente verdadeiros)
# O OPERADOR 'OU' NO PYTHON É O 'or' (apenas um precisa ser verdadeiro)