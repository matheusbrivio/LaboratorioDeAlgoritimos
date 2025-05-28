#Crie um programa que receba 10 números inteiros do usuário e os armazene em um array.
#Em seguida, o programa deve:
#Remover todos os números repetidos (manter apenas a primeira ocorrência).
#Mostrar a nova lista sem repetições.


def main():
    array = []
    for i in range (10):
        numero = int(input("Digite um numero:"))
        array.append(numero)
    testerepetiçao(array)
    print(array)
def testerepetiçao(lista):
    i = 0
    j = i + 1
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista [i] == lista[j]:
                lista.pop(j)
                lista.pop(i)
            else:
                j += 1
        i += 1
    

main()
