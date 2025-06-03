def encontrar_maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        elif lista[i] < menor:
            menor = lista[i]
    return maior, menor

valores = [8, 3, 15, 1, 22, 5]
maior, menor = encontrar_maior_menor(valores)
print("Maior número:", maior)
print("Menor número:", menor)
