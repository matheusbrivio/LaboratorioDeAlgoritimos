maiornumero = 0
menornumero = 0
posicaomaior = 0
posicaomenor = 0
numeros = []
for i in range (5):
    while True:
        try:
            numero = int(input("Digite um numero:"))
            numeros.append(numero)
            break
        except:
            print("Entrada inválida! Por favor, digite um número inteiro.")
for i in range (5):
    if i == 0:
        maiornumero = numeros[i]
        menornumero = numeros[i]
        posicaomaior = 0
        posicaomenor = 0
    else:
        if numeros[i] > maiornumero:
            maiornumero = numeros[i]
            posicaomaior = i
        if numeros[i] < menornumero:
            menornumero = numeros[i]
            posicaomenor = i
print("O maior numero é:", maiornumero)
print("O menor numero é:",menornumero)
print("O maior numero está na posição:", posicaomaior + 1, "O menor numero está na posição:", posicaomenor + 1)
