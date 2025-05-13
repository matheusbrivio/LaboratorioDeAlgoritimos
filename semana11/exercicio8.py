numeros = []
for i in range (5):
    numero = int(input("Digite um numero:"))
    while numero < 0:
        numero = int(input("Digite um numero:"))
    numeros.append(numero)

verificacao = int(input("digite um numero para verificar:"))
if verificacao in numeros:
    print("O numero está na lista!")
else:
    print("o numero nao esta na lista!")
