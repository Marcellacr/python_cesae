#verificar se os elementos estao em tamanho crescentes
numeros = []

for i in range(0,10):
    num = int(input(f"Insira os números [{i}]: "))
    numeros.append(num)

print(numeros)

if numeros[0] > numeros[1] and numeros[2] > numeros[3] > numeros[4] > numeros[5] >    \
        numeros[6] > numeros[7] > numeros[8] > numeros[9] > numeros[10]:
    print("Lista não está em ordem crescente")
else:
    print("Lista em ordem crescente")

