x=1 #int
x="CFP Cursos" #string
x= 15.6 #float
x=True #bool
n1=5;n2=2;x=complex(n1,n2) #complexos
x=["Carro","Avião","Navio", 1, 58.3, True] #LIST / Array
# x[1] = "Onibus" -> ISTO FUNCIONA
x=("Carro","Avião","Navio", 1, 58.3, True) #Tupla
# x[1] = "Onibus" -> ISTO NÃO FUNCIONA NA TUPLA
x=range(0,100,1) #LIST AUTOMATICA NÃO MODIFICÁVEL
x={
    "Canal":"CFB Cursos",
    "Curso":"Curso de python",
    "Nome": "Victor"
} #DICT

#referenciamos o DICT com:
print(x["Canal"])

x={1,23,121,22,314,1,1,1,432,3,5,2} # SET -> NÃO REPETE VALORES (PODEMOS MODIFICAR)
x=frozenset({1,23,121,22,314,1,1,1,432,3,5,2}) # FROZENSET -> NÃO REPETE VALORES (NÃO PODEMOS MODIFICAR)

#print(x)
#print("Valor: " + str(x))
#print(x.real)
#print(x.imag)
#print(x[1])
print("Tipo: " + str(type(x)))

# PARA DESCOBRIR O TIPO DA VÁRIAVEL USAMOS O 'TYPE(VARIAVEL)'
# PARA CONVERTER DE INT PARA STRING 
# PODEMOS TER NÚMEROS COMPLEXOS UTILIZANDO 'complex(xj)' ou 'complex(variavel1, variavel2)'
# CRIAMOS UMA LIST ABRINDO AS CHAVES [], E REFERENCIAMOS A QUAL ESTAMOS USANDO COM O ÍNIDICE (COMEÃ EM 0)
# A LISTA ACEITA TIPOS DE DADOS DIFERENTES DA MESMA FORMA
# NA TUPLA NÃO PODEMOS MODIFICAR ALGO
# FUNÇÃO RANGE CRIA UMA LISTA DE UM NÚMERO ATÉ OUTRO, E O TERCEIRO DIGITO É O INTERVALO ENTRE CADA ITEM
# DICT CRIA VÁRIAS VARIAVEIS QUE PODEM SER REFERENCIADAS DEPOIS
