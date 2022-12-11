valores=[1,5,3,2]
def somar(*num):
    r=0
    for n in num:
        r+=n
    return r

print(str(valores) + " a soma dos valores é: " + str(somar(valores[0],valores[1],valores[2],valores[3])))