#Escreva um programa que cria um array com os números de 1 a 10 e os imprime na ordem inversa. Faça com que receba o array e imprima. O sistema deve conter as seguintes funções:
#Preencher o array
#Mostrar o array

def preencheroarray():
    array = []
    for i in range (10):
        while True:
            try:
                numero = int(input("Digite um numero:"))
                break
            except ValueError:
                print("Tente um numero valido!")
        array.append(numero)
        print("O numero:",numero,"foi adicionado com sucesso!")
    return array

def mostrararray():
    array = preencheroarray()
    for i in range (9, - 1, -1):
        print(array[i])

mostrararray()
