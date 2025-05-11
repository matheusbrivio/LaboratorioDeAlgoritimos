numeros = []
numeros100 = []
for i in range (10):
    numero = int(input("Digite um numero:"))
    while numero in numeros:
        numero = int(input("Digite um numero:"))
    numeros.append(numero)
    if numero > 100:
        numeros100.append(numero)
print("Numeros que são maiores que 100:")
for i in range (len(numeros100)):
    print("-", numeros100[i])
    
    
print("A quantidade de numeros maiores que 100 é:", len(numeros100))
