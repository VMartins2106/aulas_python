carros=["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Onyx", "Fit"]

itCarros = iter(carros)

#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))
#print(next(itCarros))

# COM WHILE - AUTOMÁTICO

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break