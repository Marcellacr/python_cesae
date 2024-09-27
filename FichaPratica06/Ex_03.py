#ordenar tamanho crescentes
numeros=[]


for i in range(0,10):
    num = int(input(f"Insira os números [{i}]: "))
    numeros.append(num)

numeros.sort()
print(numeros)

print("O maior elemento:",numeros[9])