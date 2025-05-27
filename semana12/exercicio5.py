#Faça um algoritmo que apresente o seguinte menu:
#1 - Sacar dinheiro
#2 - Depositar dinheiro
#3 - Mostrar saldo
#4 - Sair
#O saldo inicial da conta é 0. O sistema deve ter 3 funções: Mostrar o menu; sacar; depositar; saldo


def main():
    opcao = 0
    saldomain = 0
    print("1 - SACAR DINHEIRO")
    print("2 - DEPOSITAR")
    print("3 - MOSTRAR SALDO")
    print("4 - SAIR")
    while opcao != 4:
        while True:
            try:
                opcao = int(input("Digite uma opçao:"))
                break
            except ValueError:
                print("Tente uma opçao valida!")
        if opcao == 1:
            saldomain = sacardinheiro(saldomain)
        elif opcao == 2:
            saldomain = depositardinheiro(saldomain)
        elif opcao == 3:
            print("O saldo é de R$:", saldomain)
        elif opcao == 4:
            print("Voce saiu...")
        else:
            print("Opcao invalida, tente novamente!")

def sacardinheiro(saldo):
    if saldo > 0:
        while True:
            try:
                valorsaque = float(input("Digite um valor para sacar:"))
                break
            except ValueError:
                print("Tente um valor válido!")
        if valorsaque > saldo:
            print("O valor do saque é maior do que seu saldo, tente um valor mais baixo!")
        else:
            saldo -= valorsaque
            return saldo
    print("Não é possivel sacar sem saldo!")
    return saldo


def depositardinheiro(saldo):
    while True:
            try:
                valordeposito = float(input("Digite um valor para depositar:"))
                break
            except ValueError:
                print("Tente um valor válido!")
    saldo += valordeposito
    print("Valor depositado com sucesso!")
    return saldo

main()
    
