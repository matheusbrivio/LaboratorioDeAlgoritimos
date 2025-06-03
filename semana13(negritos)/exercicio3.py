#Faça uma função que receba um número como parâmetro e retorne o seu dobro.


def main():
    n1 = int(input("Digite o numero:"))
    dobro = somanumeros(n1)
    print(dobro)

def somanumeros(n1):
    dobro = n1 * 2
    return dobro

main()
