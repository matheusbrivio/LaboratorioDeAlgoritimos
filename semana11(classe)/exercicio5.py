
tamanhoarray = int(input("Quantos numeros voce quer adicionar?"))
array1 = []
array2 = []
array3 = []

for i in range (0, tamanhoarray):
    while True:
        try:
            numero = int(input("Digite um numero para o primeiro conjunto de numeros:"))
            array1.append(numero)
            break
        except:
            print("Digite um numero inteiro!")
    
for i in range (0, tamanhoarray):
    while True:
        try:
            numero = int(input("Digite um numero para o segundo conjunto de numeros:"))
            array2.append(numero)
            break
        except:
            print("Digite um numero inteiro!")

for i in range (0, tamanhoarray):
    soma = array1[i] + array2[i]
    array3.append(soma)
    print("O numero:", array1[i], "+", "o numero:", array2[i], "é =", array3[i])
