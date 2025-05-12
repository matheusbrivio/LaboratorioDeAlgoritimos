itens = []
opcao = 0
while opcao != 5:
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    opcao = int(input("Digite a opçao desejada:"))
    if opcao == 1:
        item = input("insira um item:")
        itens.append(item)
        print("item inserido com sucesso!")
    elif opcao == 2:
        item = input("Qual item deseja retirar?")
        if item in itens:
            itens.remove(item)
            print("Item removido com sucesso!")
        else:
            print("o item nao está na lista!")
    elif opcao == 3:
        if len(itens) > 0:
            for i in range (len(itens)):
                print(itens[i])
        else:
            print("Não há itens na lista!")
    elif opcao == 4:
        itens = []
    elif opcao == 5:
        print("Voce saiu!...")
        
