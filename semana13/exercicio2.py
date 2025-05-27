#Escreva uma função que verifique se um número é primo. A função deve receber um número como parâmetro e retornar True se ele for primo, caso contrário, retorna False.

def testeprimo(numero):
    if numero < 2: return False
    for i in range(2, numero):
        if numero % i == 0: return False
    return True

def main():
    numero = int(input("Digite um numero:"))
    primo = testeprimo(numero)
    if primo == True:
        print("O numero é primo!")
    else:
        print("O numero nao é primo!")

main()
