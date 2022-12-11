a=10
b=5
op="*"
res=0

if op=="+": # VERIFICA É VERDADEIRO ///// == PARA ATRIBUIÇÃO/COMPARAÇÃO
    res=a+b

if op=="-": 
    res=a-b

if op=="*": 
    res=a*b

if op=="/": 
    res=a/b

print(str(a) + op + str(b) + " = " + str(res))