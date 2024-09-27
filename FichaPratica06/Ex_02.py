comissoes=[]

#utilizador deve inserir 10 números

for i in range(0,12):
    num = float(input(f"Insira os números [{i}]: "))
    comissoes.append(num)

print(comissoes)

comissaoTotal = sum(comissoes)

print(comissaoTotal)


#print(f"numeros[{i}]: {numeros[i]}")

