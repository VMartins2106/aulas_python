
#EXEMPLOS COM FUNÇÃO LAMBDA

soma=lambda a,b: a+b
print(soma(2,5))

mult=lambda a,b,c:(a+b)*c
print(mult(2,5,3))

print((lambda a,b:a+b)(10,20))

r=lambda x,func:x+func(x)
res = r(2,lambda x: x+3)
print(res)