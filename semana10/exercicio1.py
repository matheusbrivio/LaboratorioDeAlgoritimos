numeros = []
num30 = []
soma30 = 0
soma = 0
for i in range (8):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)
    if numero > 30:
        num30.append(numero)
for i in range (len(num30)):
    soma30 += num30[i]
for i in range (len(numeros)):
    soma += numeros[i]
print(" A quantidade de numeros maior que trinta é:", len(num30))
print("A soma dos numeros maiores que 30 é:", soma30)
print("A soma de todos os numeros é:", soma)
