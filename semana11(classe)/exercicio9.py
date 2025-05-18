import random
numeros = []
pares = 0
impares = 0
for i in range (5):
    numero = random.randint(1,100)
    numeros.append(numero)

for i in range (5):
    if numeros[i] % 2 == 0:
        print("pares:", numeros[i])
        pares += 1
    else:
        print("impares:", numeros[i])
        impares += 1
print("A quantidade total de impares é:", impares, "A quantidade total de pares é:", pares)
