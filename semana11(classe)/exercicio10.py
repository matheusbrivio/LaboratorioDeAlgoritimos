#Escreva um programa que leia dois arrays de 5 elementos inteiros cada e crie um terceiro array que seja a multiplicação dos dois primeiros arrays (elemento a elemento).

array = []
array2 = []
array3 = []

for i in range (5):
    while True:
        try:
            numero = int(input("Digite um numero:"))
            array.append(numero)
            break
        except ValueError:
            print("Tente um numero inteiro!")

for i in range (5):
    while True:
        try:
            numero = int(input("Digite um numero:"))
            array2.append(numero)
            break
        except ValueError:
            print("Tente um numero inteiro!")

for i in range (5):
    multiplicacao = array[i] * array2[i]
    array3.append(multiplicacao)
    print("O resultado da multiplicaçao:", i + 1, "=", array3[i])
            
