opcao = 0
saldo = float(input("Digite seu saldo:"))
while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Digite a sua opção!:"))
    if opcao == 1:
        subtraçao = float(input("Digite o valor que queira sacar:"))
        if subtraçao <= saldo:
            saldofinal = saldo - subtraçao
            print ("Este é seu saldo após o saque:", saldofinal)
        else:
            print ("Voce nao tem saldo suficiente para efetuar esse saque.")
    elif opcao == 2:
        adiçao = float(input("Digite o valor que queira depositar:"))
        saldofinal = saldo + adiçao
        print ("Este é seu saldo após o deposito:", saldofinal)
    elif opcao == 3:
        print("Esse é o seu saldo:", saldo)
    elif opcao == 4:
        print("Voce saiu! esperamos a sua proxima visita!.")
