import random
num_i=1
num_f=1.5
num_c=1j

num_rand=random.randrange(0,50)
# PARA CRIAR 6 NÚMEROS ALEATÓRIOS, POR EXEMPLO, USAMOS UMA LIST (ANTIGA ARRAY)
num_r=[
    random.randrange(0,50),
    random.randrange(0,50),
    random.randrange(0,50),
    random.randrange(0,50),
    random.randrange(0,50),
    random.randrange(0,50)
    ]
#REFERENCIAMOS A POSIÇÃO COM []

x=num_rand

print("Valor 1: " + str(num_r[0]))
print("Valor 2: " + str(num_r[1]))
print("Valor 3: " + str(num_r[2]))
print("Valor 4: " + str(num_r[3]))
print("Valor 5: " + str(num_r[4]))
print("Valor 6  : " + str(num_r[5]))

# PARA TRANSFORMAR EM INT USAMOS INT(VARIAVEL)
# PARA TRANSFORMAR EM FLOAT USAMOS FLOAT(VARIAVEL)
# PARA TRANSFORMAR EM STRING USAMOS STR(VARIAVEL)
# IMPORTAMOS A BIBLIOTECA RANDOM COM IMPORT RANDOM
# COM random.randrange(x,y) GERAMOS UM NÚMERO ALEATÓRIO ENTRE X E Y, DEFINIDOS POR NÓS MESMOS
