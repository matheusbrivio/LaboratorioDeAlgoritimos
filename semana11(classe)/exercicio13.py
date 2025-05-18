#Escreva um algoritmo que contenha um array e apresente o seguinte menu:
#1 - inserir item
#2 - Listar itens
#3 - Retirar item
#4- Retirar todos os itens
#5 - Contar quantos itens são maiores que um valor X (onde X é informado pelo usuário)
#6 - Verificar se um determinado número (informado pelo usuário) está presente no array
#7 - Encontrar o maior e o menor item do array
#8 - Sair
#Obs. o array só pode receber números pares. Caso o usuário digite um número ímpar, o sistema deve apresentar uma mensagem de erro e voltar para o menu.
opcao = 0
array = []
maiores = 0
maiornumero = 0
menornumero = 0
while opcao != 8:
    print("#1 - Inserir item")
    print("#2 - Listar itens")
    print("#3 - Retirar item")
    print("#4 - Retirar todos os itens")
    print("#5 - Contar quantos itens são maiores que um valor X")
    print("#6 - Verificar se um número está presente no array")
    print("#7 - Encontrar o maior e o menor item do array")
    print("#8 - Sair")
    opcao = int(input("Digite a opção:"))
    if opcao == 1:
        inserir = int(input("Digite o numero a ser inserido:"))
        if inserir % 2 == 0:
            array.append(inserir)
            print("O elemento:", inserir, "foi inserido com sucesso!")
        else:
            print("O numero inserido não é par! tente inserir um numero par.")
    elif opcao == 2:
        if len(array) > 0:
            print("A lista de itens é:", array)
        else:
            print("Voce ainda nao tem itens!")
    elif opcao == 3:
        print(array)
        remover = int(input("Digite o item que deseja remover:"))
        array.remove(remover)
        print("Item removido com sucesso!")
    elif opcao == 4:
        array.clear()
        print("Lista limpa com sucesso!")
    elif opcao == 5:
        maiorverificar = int(input("Digite qual numero deseja verificar se é maior:"))
        for i in range (len(array)):
            if array[i] > maiorverificar:
               maiores += 1
               print("O numero:", array[i], "é maior que:", maiorverificar)
            
        if maiores == 0:
            print("Não há numeros maiores que:", maiorverificar)
    elif opcao == 6:
        numeropresente = int(input("Digite o numero a ser verificado se está presente:"))
        if numeropresente in array:
            print("O numero está presente na lista!")
        else:
            print("O numero nao está presente na lista!")
    elif opcao == 7:
        for i in range(len(array)):
            if i == 0:
                maiornumero = array[i]
                menornumero = array[i]
            elif array[i] > maiornumero:
                maiornumero = array[i]
            elif array[i] < menornumero:
                menornumero = array[i]
        print("O maior numero é:", maiornumero, "O menor numero é:", menornumero)
    elif opcao == 8:
        print("Voce saiu...")
    else:
        print("Insira uma opção válida!")
