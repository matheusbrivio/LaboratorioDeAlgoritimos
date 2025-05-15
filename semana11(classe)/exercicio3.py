array = []
soma = 0
for i in range (5):
    numero = int(input("Digite um numero:"))
    array.append(numero)
for i in range (5):
    soma += array[i]

media = soma / (len(array))
print("A media dos numeros é:",media)
