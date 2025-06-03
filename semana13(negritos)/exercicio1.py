#Escreva uma função que receba dois números como parâmetros e retorne a soma deles.

def main():
    n1 = int(input("Digite o primeiro numero:"))
    n2 = int(input("Digite o segundo numero:"))
    soma = somanumeros(n1,n2)
    print(soma)

def somanumeros(n1,n2):
    soma = n1 + n2
    return soma

main()
