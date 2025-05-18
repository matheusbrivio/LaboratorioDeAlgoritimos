import random
numeros = []

for i in range (10):
    numero = random.randint(1,100)
    numeros.append(numero)

for i in range (10):
    if numeros[i] % 2 == 0:
        print(numeros[i])

