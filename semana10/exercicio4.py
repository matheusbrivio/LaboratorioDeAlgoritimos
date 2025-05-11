vetorA = []
vetorB = []

for i in range (10):
    numero = int(input("Digite um numero:"))
    while numero in vetorA:
        numero = int(input("Digite um numero:"))
    vetorA.append(numero)

for i in range (9, -1, - 1):
    vetorB.append(vetorA[i])

print(vetorA)
print(vetorB)
