numeros = []
numeromultiplicado = []
numeromultiplicar = int(input("qual numero voce quer que seja o multiplicador?:"))
for i in range (6):
    numero = int(input("Digite um numero:"))
    numeros.append(numero)

for i in range (6):
    numerofinal = numeros[i] * numeromultiplicar
    numeromultiplicado.append(numerofinal)
    print(numeromultiplicado[i])
