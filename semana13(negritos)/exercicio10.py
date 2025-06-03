def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    numeros = []
    for i in range(10):
        valor = int(input("Digite um número: "))
        numeros.append(valor)

    for i in range(len(numeros)):
        if eh_primo(numeros[i]):
            print(numeros[i])

main()
