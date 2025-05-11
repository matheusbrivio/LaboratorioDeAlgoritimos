numeros = []
for i in range (10):
    numero = int(input("Digite um numero:"))
    while numero in numeros:
        numero = int(input("Digite um numero:"))
    numeros.append(numero)
print("os numeros pares são:")
for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], "Posição:", i + 1)
