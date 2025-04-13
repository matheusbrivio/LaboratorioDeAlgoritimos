contador = 0
maior30menor90 = 0
while contador < 10:
    numeros = int(input("Digite o numero:"))
    if numeros >=  30 and numeros <= 90:
        maior30menor90 += 1

    contador += 1
print("A quantidade de numeros maior que 30 e menor que 90 é:", maior30menor90)
