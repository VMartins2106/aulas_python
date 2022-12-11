
def somar(n1,n2,n3,n4):
    r=n1+n2+n3+n4
    print("A soma de valores é " + str(r))

somar(1,7,6,1)
somar(10,2,192,3)
somar(128,8,1,8)

# EXEMPLO COM ARGS

def somar(*num):
    r=0
    for n in num:
        r+=n
    print("A soma é: " + str(r))

somar(6,1,5,12,5,12,3412,4,123,124,123,23,132)