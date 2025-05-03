pares = 0
impares = 0
zeros = 0

for i in range (10):
    numero = int(input("digite um numero"))
    if numero % 2 == 0:
        pares += 1
    elif numero % 2 == 1:
        impares += 1
    if numero == 0:
        zeros += 1
print (pares,impares,zeros)
