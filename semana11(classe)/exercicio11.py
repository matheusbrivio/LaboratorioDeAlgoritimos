#Escreva um programa que leia um array de 5 elementos e determine se todos os elementos são distintos (não há elementos repetidos).

array = []
repetidos = []
for i in range (5):
    elemento = input("Digite um elemento:")
    if elemento in array:
        print("O elemento:", elemento, "ja está no array!")
        repetidos.append(elemento)
    array.append(elemento)
print("Os elementos do array são:", array)
print("Os elementos repetidos são:", repetidos)
    
