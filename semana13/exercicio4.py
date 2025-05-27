#Faça uma função que receba um número como parâmetro e retorne a soma de todos os números naturais menores ou iguais a ele.

def main():
    numero = int(input("Digite um numero:"))
    somanumero = somanumeros(numero)
    print(somanumero)
def somanumeros(numero):
    soma = 0
    for i in range (numero, -1, -1):
        soma += numero + (numero - i)
    return soma

main()
