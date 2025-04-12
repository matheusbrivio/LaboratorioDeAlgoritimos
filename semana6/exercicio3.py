numero = int(input("Digite um numero:"))
contador = 0
while numero != 0:
    if numero == 10:
        contador += 1
    numero = int(input("Digite um numero:"))
print ("O numero de numeros 10 foi repetido:",contador, "vezes")
