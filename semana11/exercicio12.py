numeros = []
for i in range (15):
    numero = int(input("Digite um numero:"))
    while numero in numeros:
        print("o numero está na lista!")
        numero = int(input("Digite um numero:"))
    numeros.append(numero)

print(numeros)

